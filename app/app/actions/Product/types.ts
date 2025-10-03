export type ProductIndexActionPropTypes = {
  products?: {
    name: string
    id: string
    category: string
    tags: string[]
  }[]
  errors?: string
}