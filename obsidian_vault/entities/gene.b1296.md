---
entity_id: "gene.b1296"
entity_type: "gene"
name: "puuP"
source_database: "NCBI RefSeq"
source_id: "gene-b1296"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1296"
  - "puuP"
---

# puuP

`gene.b1296`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1296`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

puuP (gene.b1296) is a gene entity. It encodes puuP (protein.P76037). Encoded protein function: FUNCTION: Involved in the uptake of putrescine (PubMed:15590624, PubMed:19181795, PubMed:23719730, PubMed:27803167). Imports putrescine for its utilization as an energy source in the absence of glucose (PubMed:23719730). {ECO:0000269|PubMed:15590624, ECO:0000269|PubMed:19181795, ECO:0000269|PubMed:23719730, ECO:0000269|PubMed:27803167}. EcoCyc product frame: B1296-MONOMER. EcoCyc synonyms: ycjJ. Genomic coordinates: 1357802-1359187. EcoCyc protein note: PuuP is a proton dependent putrescine transporter which functions in the exponential growth phase . Mutational experiments show that among all the genes for putrescine transport (potFGHI, potABCD, potE and puuP) only puuP is essential to utilise putrescine as a sole carbon or nitrogen source . The level of puuP expression increases at low concentrations of glucose (0.04%). The expression of puuP is not inhibited by the intracellular accumulation of putrescine . PuuP and YEEF-MONOMER PlaP are receptors for the group 5 CDI ionophore toxins .

## Biological Role

Repressed by puuR (protein.P0A9U6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76037|protein.P76037]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A9U6|protein.P0A9U6]] `RegulonDB` `C` - regulator=PuuR; target=puuP; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004362,ECOCYC:G6643,GeneID:946287`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1357802-1359187:-; feature_type=gene
