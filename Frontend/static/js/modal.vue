<script type="text/x-template" id="modalheader">
    <h5 class="modal-title" id="exampleModalLongTitle">{{title}}</h5>
    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
        <span aria-hidden="true">&times;</span>
    </button>
</script>

<script type="text/x-template" id="createmodalfooter">
    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
    <button type="button" class="btn btn-primary" @click="create">Create</button>
</script>

<script type="text/x-template" id="createmodalbody">
    <input type="text" id="title"/>
    <textarea type="text" id="content"></textarea>
</script>

<script type="text/x-template" id="createmodalfooter">
    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
    <button type="button" class="btn btn-primary" @click="create">{{action}}</button>
</script>

<script type="text/x-template" id="updatemodalfooter">
    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
    <button type="button" class="btn btn-primary" @click="update">{{action}}</button>
</script>

<script type="text/x-template" id="updatemodalfooter">
    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
    <button type="button" class="btn btn-primary" @click="delete">{{delete}}</button>
</script>

Vue.component('modalheader', {
    props: ['title'],
    template: '#createmodalheader'
})

Vue.component('createmodalbody', {
    props: ['data'],
    template: '#createmodalbody'
})

Vue.component('createmodalfooter', {
    props: ['action'],
    template: '#createmodalfooter'
})

Vue.component('updatemodalfooter', {
    props: ['action'],
    template: '#createmodalfooter'
})

Vue.component('deletemodalbody', {
    props: ['data'],
    template: '#createmodalbody'
})

Vue.component('modalfooter', {
    props: ['data'],
    template: '#createmodalfooter'
})