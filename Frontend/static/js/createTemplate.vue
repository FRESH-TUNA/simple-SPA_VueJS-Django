<template>
    <form>
        <div class="form-group">
            <label for="title">Title</label>
            <input type="text" class="form-control" placeholder="Enter title" v-model:value="currentViewData.title">
        </div>
        <div class="form-group">
            <label for="content">Content</label>
            <textarea class="form-control"  v-model:value="currentViewData.content"></textarea>
        </div>
        <button type="button" class="btn btn-primary" @click="mainview.createPost(currentViewData.title,currentViewData.content,currentViewData.id)">Submit</button>
    </form>
</template>

<script>
module.exports = {
    props: ['currentViewData'],
    data: function() {
        return {
            
        }
    },
}
</script>

<style scoped>
    textarea {
        height: 300px;
    }
</style>