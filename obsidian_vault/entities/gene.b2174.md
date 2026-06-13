---
entity_id: "gene.b2174"
entity_type: "gene"
name: "lpxT"
source_database: "NCBI RefSeq"
source_id: "gene-b2174"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2174"
  - "lpxT"
---

# lpxT

`gene.b2174`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2174`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lpxT (gene.b2174) is a gene entity. It encodes lpxT (protein.P76445). Encoded protein function: FUNCTION: Involved in the modification of the lipid A domain of lipopolysaccharides (LPS). Transfers a phosphate group from undecaprenyl pyrophosphate (C55-PP) to lipid A to form lipid A 1-diphosphate. Contributes to the recycling of undecaprenyl phosphate (C55-P) (PubMed:18047581). In vitro, has low undecaprenyl-diphosphate phosphatase activity (PubMed:17660416). {ECO:0000269|PubMed:17660416, ECO:0000269|PubMed:18047581}. EcoCyc product frame: G7146-MONOMER. EcoCyc synonyms: yeiU. Genomic coordinates: 2268854-2269567. EcoCyc protein note: LpxT transfers a phosphate group from undecaprenyl-pyrophosphate (Und-PP or C55-PP) to the position 1 phosphate of approximately one-third of lipid A-core oligosaccharide molecules to create lipid A-core 1-diphosphate. LpxT activity enhances the net negative charge of LPS and contributes to recycling of the carrier lipid CPD-9646 that is required for biosynthesis of a number of cell wall polymers such as peptidoglycan and lipopolysaccharide...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76445|protein.P76445]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=lpxT; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007196,ECOCYC:G7146,GeneID:946693`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2268854-2269567:+; feature_type=gene
