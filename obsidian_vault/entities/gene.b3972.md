---
entity_id: "gene.b3972"
entity_type: "gene"
name: "murB"
source_database: "NCBI RefSeq"
source_id: "gene-b3972"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3972"
  - "murB"
---

# murB

`gene.b3972`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3972`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

murB (gene.b3972) is a gene entity. It encodes murB (protein.P08373). Encoded protein function: FUNCTION: Cell wall formation. EcoCyc product frame: UDPNACETYLMURAMATEDEHYDROG-MONOMER. EcoCyc synonyms: yijB. Genomic coordinates: 4172057-4173085. EcoCyc protein note: UDP-N-acetylenolpyruvoylglucosamine reductase (MurB) catalyzes the second committed step in the biosynthesis of peptidoglycan. The enzyme is essential for growth and is a target for development of new antibiotics . Crystal structures of the enzyme have been solved , and the NADP+ binding site has been localized by NMR and appears to co-localize with the binding pocket for UDP-N-acetylenolpyruvoylglucosamine . The kinetic mechanism of the enzyme has been investigated. The reaction appears to proceed as a sequence of two half-reactions . MurA, MurB and MurC are capable of chemo-enzymatic labeling and modifying of UDP-GlcNAc-RNA in vitro . Reviews:

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08373|protein.P08373]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012999,ECOCYC:EG11205,GeneID:948470`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4172057-4173085:+; feature_type=gene
