---
entity_id: "gene.b4193"
entity_type: "gene"
name: "ulaA"
source_database: "NCBI RefSeq"
source_id: "gene-b4193"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4193"
  - "ulaA"
---

# ulaA

`gene.b4193`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4193`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ulaA (gene.b4193) is a gene entity. It encodes ulaA (protein.P39301). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II UlaABC PTS system is involved in ascorbate transport. {ECO:0000269|PubMed:12644495, ECO:0000305|PubMed:11741871}. EcoCyc product frame: SGAT-MONOMER. EcoCyc synonyms: yjfS, sgaT. Genomic coordinates: 4419980-4421377. EcoCyc protein note: UlaA is the integral membrane component of the ascorbate PTS system. Crystal structures, thought to represent an outward open, substrate bound and an occluded, substrate bound conformation have been reported. The protein crystallises as a dimer; ascorbate is bound, through a mixture of hydrogen and van der Waals intereactions, in a pocket located in the 'core domain' of the dimer; the UlaA protomer contains 11 transmembrane segments, 4 hairpin like structures and three amphipathic helices . A ulaA deletion mutant is unable to transport or ferment L-ascorbate in vivo or to phosphorylate L-ascorbate in vitro . ulaA: utilization of L-ascorbate

## Biological Role

Repressed by ulaR (protein.P0A9W0). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39301|protein.P39301]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=ulaA; function=+
- `represses` <-- [[protein.P0A9W0|protein.P0A9W0]] `RegulonDB` `C` - regulator=UlaR; target=ulaA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013723,ECOCYC:G7856,GeneID:948717`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4419980-4421377:+; feature_type=gene
