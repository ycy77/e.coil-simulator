---
entity_id: "gene.b2068"
entity_type: "gene"
name: "alkA"
source_database: "NCBI RefSeq"
source_id: "gene-b2068"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2068"
  - "alkA"
---

# alkA

`gene.b2068`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2068`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

alkA (gene.b2068) is a gene entity. It encodes alkA (protein.P04395). Encoded protein function: FUNCTION: Hydrolysis of the deoxyribose N-glycosidic bond to excise 3-methyladenine, 3-methylguanine, 7-methylguanine, O2-methylthymine, and O2-methylcytosine from the damaged DNA polymer formed by alkylation lesions. EcoCyc product frame: EG11222-MONOMER. EcoCyc synonyms: aidA. Genomic coordinates: 2146692-2147540. EcoCyc protein note: The alkA gene product is known as 3-methyl-adenine-DNA glycosylase II and is induced by exposure to alkylating agents as part of the cell's adaptive response to damage caused by alkylation. The purified enzyme acts preferentially on dsDNA to remove 3-methyl-adenine and 3-methyl-guanine with equal efficiency and also removes, somewhat less efficiently, 7-methyl-adenine, 7-methyl-guanine, 2-methyl-thymine and their ethylated derivatives . AlkA is one of two (along with 3-methyl-adenine DNA glycosylase I, the tag gene product) glycosylases that remove 3-methyl-adenines. Glycosylase II differs in two ways: it can remove several other methylated bases besides 3-methyl-adenine and it is inducible to a 20-fold higher level in cells exposed to alkylating agents . Additional roles for AlkA were found through studies on removal of deaminated adenine residues and studies on repair of oxidative damage. AlkA was found to be the hypoxanthine DNA glycosylase in E...

## Biological Role

Activated by rpoD (protein.P00579), ada (protein.P06134), rpoS (protein.P13445).

## Enriched Pathways

- `eco03410` Base excision repair (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P04395|protein.P04395]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=alkA; function=+
- `activates` <-- [[protein.P06134|protein.P06134]] `RegulonDB` `C` - regulator=Ada; target=alkA; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=alkA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006848,ECOCYC:EG11222,GeneID:947371`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2146692-2147540:-; feature_type=gene
