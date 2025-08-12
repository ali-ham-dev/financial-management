<script setup lang="ts">
  import { ref, onMounted } from 'vue';  
  
  const name = ref("John Doe");
  const status = ref("active");
  const tasks = ref(["Task 1", "Task 2", "Task 3"]);
  const newTask = ref("");

  const toggleStatus = () => {
    if (status.value === "active") {
      status.value = "pending";
    } else if (status.value === "pending") {
      status.value = "inactive";
    } else {
      status.value = "active";
    }
  }

  const addTask = () => {
    if (newTask.value.trim() !== "") {
      tasks.value.push(newTask.value);
      newTask.value = "";
    }
  }

  const deleteTask = (index: number): void => {
    tasks.value.splice(index, 1);
  }

  onMounted(async () => {
    try {
      const response = await fetch("https://jsonplaceholder.typicode.com/todos");
      const data = await response.json();
      tasks.value = data.map((task: any) => task.title)
      console.log(data);
    } catch (error) {
      console.error("Error fetching tasks:", error);
    }
  })
</script>

<template>
  <h1>FinManag</h1>
  <p v-if="status === 'active'">User is active</p>
  <p v-else-if="status === 'pending'">User is pending</p>
  <p v-else>User is not active</p>

  <form @submit.prevent="addTask">
    <label for="newTask">New Task</label>
    <input type="text" id="newTask" name="newTask" v-model="newTask" />
    <button type="submit">Submit</button>
  </form>

  <h3>Tasks</h3>
  <ul>
    <li v-for="(task, index) in tasks" :key="task">
      <span>
        {{ task }}
        <button @click="deleteTask(index)">X</button>
      </span>
    </li>
  </ul>

  <!-- <button v-on:click="toggleStatus">Toggle Status</button> -->
  <button @click="toggleStatus">Toggle Status</button>
</template>

<style scoped>

</style>
