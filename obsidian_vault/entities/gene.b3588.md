---
entity_id: "gene.b3588"
entity_type: "gene"
name: "aldB"
source_database: "NCBI RefSeq"
source_id: "gene-b3588"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3588"
  - "aldB"
---

# aldB

`gene.b3588`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3588`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aldB (gene.b3588) is a gene entity. It encodes aldB (protein.P37685). Encoded protein function: FUNCTION: Catalyzes the NADP(+)-dependent oxidation of diverse aldehydes to their corresponding carboxylic acids, with a preference for acetaldehyde and chloroacetaldehyde (PubMed:15659684). May play a role in detoxifying aldehydes present during stationary phase (Probable). Cannot use NAD(+) instead of NADP(+) as the electron acceptor. To a lesser extent is also able to oxidize propionaldehyde (propanal), benzaldehyde, mafosfamide, and 4-hydroperoxycyclophosphamide. Does not use either glyceraldehyde or glycolaldehyde as substrates (PubMed:15659684). {ECO:0000269|PubMed:15659684, ECO:0000305|PubMed:7768815}. EcoCyc product frame: ALDDEHYDROGB-MONOMER. EcoCyc synonyms: yiaX. Genomic coordinates: 3754973-3756511.

## Biological Role

Repressed by fis (protein.P0A6R3). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37685|protein.P37685]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=aldB; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=aldB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011718,ECOCYC:EG12292,GeneID:948104`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3754973-3756511:-; feature_type=gene
