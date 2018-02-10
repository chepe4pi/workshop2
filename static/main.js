window.onload = function () {
  new Vue({
      el: '#song',
      data: {
        items: []
      },
      created: function () {
          const vm = this;
          axios.get('/songs')
              .then(function (response) {
                  vm.items = response.data
              })
      }
  })
};
