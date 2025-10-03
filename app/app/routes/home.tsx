import { useFetcher, useLoaderData, type ActionFunction, type ActionFunctionArgs, type FetcherWithComponents, type LoaderFunction, type LoaderFunctionArgs } from "react-router";
import { ProductIndexLoader, type ProductIndexLoaderPropTypes } from "../loaders";
import type { Route } from "./+types/home";
import { ACTION_CONST, FETCHER_KEYS } from "../utils";
import React from "react";
import { productIndexActionHandler, type ProductIndexActionPropTypes } from "../actions";

export function meta ({ }: Route.MetaArgs) {
  return [
    { title: "Remarcable coade assignment" },
    { name: "description", content: "Remarcable coade assignment" },
  ];
}

export const loader: LoaderFunction = async ({
  request,
}: LoaderFunctionArgs): Promise<ProductIndexLoaderPropTypes> =>
  ProductIndexLoader(request);

export const action: ActionFunction = async ({
  request,
}: ActionFunctionArgs): Promise<ProductIndexActionPropTypes> =>
  productIndexActionHandler(request);


export default function Home () {
  const loaderData: ProductIndexLoaderPropTypes = useLoaderData();

  const projectFetcherData: FetcherWithComponents<ProductIndexActionPropTypes> = useFetcher({ key: FETCHER_KEYS.PROJECTS });


  return (
    <projectFetcherData.Form method="post" className="p-4">
      <div className="flex  gap-4 mb-4">
        <div>
          <p>Catergories:</p>
          {loaderData.filters.categories.map((category) => (
            <div className="flex gap-2" key={category}>
              <input
                id={`category-${category}`}
                type="checkbox"
                value={category}
                name={`category-${category}`}
              />
              <label className="flex items-center gap-2" htmlFor={`category-${category}`}>
                {category}
              </label>
            </div>
          ))}
        </div>

        <div>
          <p>tags:</p>
          <div>
            {loaderData.filters.tags.map((tag) => (
              <div className="flex gap-2" key={tag}>
                <input
                  id={`tag-${tag}`}
                  type="checkbox"
                  value={tag}
                  name={`tag-${tag}`}
                />
                <label className="flex items-center gap-2">
                  {tag}
                </label>
              </div>
            ))}
          </div>
        </div>

        <div>
          <label htmlFor="search">Search: </label>
          <input type='text' name='search' placeholder="Search by name" className="border border-gray-300 rounded px-2 py-1 mb-4" />
        </div>
      </div>

      <button
        type="submit"
        name="_action"
        value={ACTION_CONST.GET_PROJECTS}
        className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 mb-4"
      >
        Filter
      </button>

      <table className="table-auto border-collapse border border-slate-400 w-full max-w-[600px]">
        <thead>
          <tr className="bg-gray-200 text-left">
            <th>
              Name
            </th>
            <th>Category</th>
            <th>Tags</th>
          </tr>
        </thead>
        <tbody>
          {(projectFetcherData?.data?.products || loaderData.products).map(product => (
            <tr key={product.id}>
              <td>{product.name}</td>
              <td>{product.category}</td>
              <td>{product.tags.join(', ')}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </projectFetcherData.Form>
  )
}
