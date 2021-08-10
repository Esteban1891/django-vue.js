<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/facturaxion.png">
    <HelloWorld msg="Esteban Omar Mora Delgado "/>
    <file-upload></file-upload>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import FileUpload from './components/FileUpload.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
    FileUpload
  }
}
</script>

<style>
@import './assets/css/css.css';
</style>
