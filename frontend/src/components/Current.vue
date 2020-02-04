<template>
  <div class="current d-flex align-items-center justify-content-center">
    {{ current }}°C
  </div>
</template>

<script>
export default {
  name: 'Current',
  data () {
    return {
      current: 100
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .current {
    height: 100vh;
    font-size: 24px;
  }
</style>
