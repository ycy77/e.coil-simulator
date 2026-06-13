---
entity_id: "gene.b2938"
entity_type: "gene"
name: "speA"
source_database: "NCBI RefSeq"
source_id: "gene-b2938"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2938"
  - "speA"
---

# speA

`gene.b2938`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2938`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

speA (gene.b2938) is a gene entity. It encodes speA (protein.P21170). Encoded protein function: FUNCTION: Catalyzes the biosynthesis of agmatine from arginine. {ECO:0000269|PubMed:19603287, ECO:0000269|PubMed:2198270, ECO:0000269|PubMed:4571773}. EcoCyc product frame: ARGDECARBOXBIO-MONOMER. Genomic coordinates: 3083935-3085911. EcoCyc protein note: Biosynthetic arginine decarboxylase (SpeA) carries out the first step in PWY-40, the decarboxylation of L-arginine to yield agmatine . This enzymatic activity is subject to feedback inhibition by the downstream polyamine products putrescine and spermidine . SpeA is specific to arginine, and can neither decarboxylate nor be inhibited by L-ornithine or L-lysine . The active form of SpeA is a tetramer with one molecule of pyridoxal 5' phosphate bound per subunit . This tetrameric conformation depends on the presence of the Mg2+ cofactor. In its absence, arginine decarboxylase exists in equilibrium between the monomeric and dimeric forms, with the exact distribution of forms depending on pH . A crystal structure of SpeA has been solved at 3.1 Å resolution and shows a dimer-of-dimers arrangement . In experiments with an E. coli W strain, showed that putrescine biosynthesis preferentially utilized exogenously added arginine. Cells grown with exogenous arginine preferentially utilize the PWY-40 (SpeA-SpeB) pathway...

## Biological Role

Repressed by purR (protein.P0ACP7).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P21170|protein.P21170]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACP7|protein.P0ACP7]] `RegulonDB` `S` - regulator=PurR; target=speA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009634,ECOCYC:EG10959,GeneID:947432`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3083935-3085911:-; feature_type=gene
