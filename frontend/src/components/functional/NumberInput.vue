<!-- Component to add/substract certain parameters.

How to use:

<NumberInput :min = 5 :max = 10></NumberInput>
min nad max are optional, to define limits of the changer

<NumberInput
      v-for="item in fetchedItems"
      :key="item.id"
      :value="item.someValue"
    ></NumberInput>
-->

<template>
  <div style="text-align: center;">
  <div style="text-align:center; text-decoration: overline; font-style: oblique; font-weight: 600;">{{ name }}</div>
  <button
  class="value-control"
  @click = "stepDown"
  title="Decrease value"
  aria-label="Decrease value">-</button>

<input
  class="value-input"
  type="number"
  v-model="inputValue"
  name="numberInput"
  :min = "min"
  :max = "max"
  @input="onInput"
  ref = "inputRef"
  id="numberInput" readonly>

<button
  class="value-control"
  @click="stepUp"
  title="Increase value"
  aria-label="Increase value">+</button>
</div>

</template>

<style scoped>

.value-control {
  margin: 0 0.1rem;
  padding: 0.5rem;
  background: transparent;
  border: 0.1rem solid #817474;;
  border-radius: 0.3rem;
  color: #6c5c5c;
  cursor: pointer;
}

.value-control:hover {
  background: #eee;
}

.value-control:active {
  background: #ddd;
}

.value-control:focus,
.value-input:focus {
  outline: 2px solid #b90606;
  outline-offset: 1px
}

.value-input {
  margin: 0;
  width: 35%;
  border: 0.3rem double red;
  border-radius: 0.8rem;
  padding: 0.5rem;
  text-align: center;
}

.value-input:hover {
  border-color: #777;
}
</style>

<script>
export default {
  props: {
    min: {
      type: Number,
      default: 0, // Default min value
    },
    max: {
      type: Number,
      default: 10, // Default max value
    },
    value: {
      type: Number,
      //default: 0,
    },
    name: {
      type: String,
      default: "Empty label",
    }

  },
  data() {
    return {
      inputValue: this.value,
    };
  },
  watch: {
    value(newVal) {
      this.inputValue = newVal;
    },
    inputValue(newVal) {
      this.$emit('update:value', newVal);
    }
  },
  methods: {
    stepUp() {
      const input = this.$refs.inputRef;
      if (input && typeof input.stepUp === 'function') {
        input.stepUp();
        this.inputValue = Number(input.value);
      }
    },
    stepDown() {
      const input = this.$refs.inputRef;
      if (input && typeof input.stepDown === 'function') {
        input.stepDown();
        this.inputValue = Number(input.value);
      }
    },
  },
};
</script>
