from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)
    host = "http://127.0.0.1:8000"

    def on_start(self):
        response = self.client.post("/trainers/", json={"name": "usertest", "birthdate": "2026-02-23"})
        if response.status_code == 200 or response.status_code == 201:
            self.trainer_id = response.json().get("id", 1)
        else:
            print(f"Échec on_start: {response.status_code} - {response.text}")
            self.trainer_id = 1

    @task(1)
    def post_new_trainer(self):
        self.client.post("/trainers/", json={"name": "mehmoud", "birthdate": "2026-02-23"})

    @task(3)
    def get_trainers_id(self):
        self.client.get(f"/trainers/{self.trainer_id}", name="/trainers/{trainer_id}")
    
    @task(2)
    def post_trainers_item(self):
        self.client.post(f"/trainers/{self.trainer_id}/item/")