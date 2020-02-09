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
  },
  mounted () {
    let chatSocket = new WebSocket('ws://' + window.location.host + '/ws/current/')

    chatSocket.onmessage = function (e) {
      console.log(e)
      // let data = JSON.parse(e.data)
      // let message = data['message']
      // document.querySelector('#chat-log').value += (message + '\n')
    }

    chatSocket.onclose = function () {
      console.error('Chat socket closed unexpectedly')
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
