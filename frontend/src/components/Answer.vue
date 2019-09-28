<template>
    <div>
        <p class="text-muted">
            <strong>{{ answer.author }} </strong> &#8901; {{ answer.created_at }}
        </p>
        <p>{{ answer.body }}</p>
        <div v-if="isAnswerAuthor">
             <router-link :to="{name: 'answer-editor', params: {id: answer.id}}"
             class="btn btn-sm btn-outline-secondary mr-1">Edit</router-link>
             <button class="btn btn-sm btn-outline-danger" @click="triggerDeleteAnswer" >Delete</button>
        </div>
        <div v-else>
            <button class="btn btn-sm"
            @click="toggleLike"
            :class="{'btn-danger': userLikedAnswer,
                     'btn-outline-danger': !userLikedAnswer
                     }">
            <strong>Like</strong>
            </button>
        </div>
        <hr>
    </div>
</template>


<script>
export default {
    name: "AnswerComponent",
    props: {
        answer: {
            type: Object,
            required: true
        },
        requestUser: {
           type: String,
           required: true
        }
    },
    data() {
        return {
            userLikedAnswer: this.answer.user_has_voted,
            likesNumber: this.answer.likes_count
        }
    },
    computed: {
        toggleLike() {
            this.userLikedAnswer === false
            ? this.likeAnswer()
            : this.unlikeAnswer()
        },
        likeAnswer() {
            this.userLikedAnswer = true;
            this.likesCounter += 1;
            let endpoint = `/api/answers/${this.answer.id}`
        },
        unlikeAnswer() {

        },
        isAnswerAuthor() {
            return this.answer.author === this.requestUser;
        }
    },
    methods: {
        triggerDeleteAnswer() {
            this.$emit("delete-answer", this.answer)
        }
    }
}
</script>