export type ProductIndexLoaderPropTypes = {
  products: {
    name: string
    id: string
    category: string
    tags: string[]
  }[]
  filters: {
    tags: string[]
    categories: string[]
  }
}