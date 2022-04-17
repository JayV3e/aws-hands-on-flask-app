<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Things people are thankful for ...</h1>
        <hr><br><br>
        <button
          type="button"
          class="btn btn-success btn-sm"
          v-b-modal.thankful-modal>
          Add something you are thankful for today...
        </button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Date</th>
              <th scope="col">Author</th>
              <th scope="col">Thankful for</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="(thankful, index) in thankfuls"
              :key="index"
            >
              <td>{{ thankful.Date }}</td>
              <td>{{ thankful.Author }}</td>
              <td>{{ thankful.Thankful }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal
    ref="addThankfulModal"
    id="thankful-modal"
    title="Add something you are thankful for..."
    name=""
    hide-footer>
    <b-form
    @submit="onSubmit"
    @reset="onReset"
    class="w-100">
    <b-form-group
      id="form-author-group"
      label="Author:"
      label-for="form-author-input">
      <b-form-input
        id="form-author-input"
        type="text"
        v-model="addThankfulForm.Author"
        required
        placeholder="Who are you ?"
      >
      </b-form-input>
    </b-form-group>
    <b-form-group
      id="form-thankful-group"
      label="Thankful:"
      label-for="form-thankful-input"
    >
      <b-form-input
        id="form-thankful-input"
        type="text"
        v-model="addThankfulForm.Thankful"
        required
        placeholder="What are you thankful for today ?"
      >
      </b-form-input>
    </b-form-group>
    <b-button-group>
    <b-button
        type="submit"
        variant="primary"
    >Submit</b-button>
    <b-button
        type="reset"
        variant="danger"
    >Reset</b-button>
    </b-button-group>
    </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Thankful',
  data() {
    return {
      thankfuls: [],
      addThankfulForm: {
        Author: '',
        Thankful: '',
      },
    };
  },
  methods: {
    getThankful() {
      const path = 'http://127.0.0.1:5000/';
      axios.get(path)
        .then((res) => {
          this.thankful = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    addThankful(payload) {
      const path = 'http://127.0.0.1:5000/';
      axios
        .post(path, payload)
        .then(() => {
          this.getThankful();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getThankful();
        });
      console.log(payload);
    },
    initForm() {
      this.addThankfulForm.Author = '';
      this.addThankfulForm.Thankful = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addThankfulModal.hide();
      const payload = {
        author: this.addThankfulForm.Author,
        thankful: this.addThankfulForm.Thankful,
      };
      this.addThankful(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addThankfulModal.hide();
      this.initForm();
    },
  },

  created() {
    this.getThankful();
  },
};
</script>
