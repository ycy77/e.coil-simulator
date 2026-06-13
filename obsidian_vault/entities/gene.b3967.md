---
entity_id: "gene.b3967"
entity_type: "gene"
name: "murI"
source_database: "NCBI RefSeq"
source_id: "gene-b3967"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3967"
  - "murI"
---

# murI

`gene.b3967`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3967`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

murI (gene.b3967) is a gene entity. It encodes murI (protein.P22634). Encoded protein function: FUNCTION: Provides the (R)-glutamate required for cell wall biosynthesis. {ECO:0000255|HAMAP-Rule:MF_00258, ECO:0000269|PubMed:1355768, ECO:0000269|PubMed:8098327, ECO:0000305|PubMed:17568739}. EcoCyc product frame: GLUTRACE-MONOMER. EcoCyc synonyms: yijA, dga, glr. Genomic coordinates: 4165428-4166285. EcoCyc protein note: Glutamate racemase (MurI) catalyzes the racemization of L-glutamate to D-glutamate, an essential component that is unique to bacterial peptidoglycan . Physiological concentrations of UDP-N-acetylmuramyl-L-Ala, the second substrate of the subsequent reaction in peptidoglycan biosynthesis, specifically activates the enzyme . It was suggested that the unique N terminus of MurI is required for activation ; however, an N-terminally truncated enzyme is still activated by UDP-N-acetylmuramyl-L-Ala . Site-directed mutagenesis of the two conserved cysteine residues showed that they are essential for enzymatic activity, suggesting that they are involved in the two-base reaction mechanism . Evidence regarding the quarternary structure of MurI was contradictory: reported a homodimer, while report that the enzyme is monomeric. A crystal structure of MurI in complex with UDP-N-acetylmuramyl-L-Ala has been solved at 1.9 Å resolution and shows a monomer...

## Biological Role

Repressed by gadX (protein.P37639). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00470` D-Amino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P22634|protein.P22634]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=murI; function=+
- `represses` <-- [[protein.P37639|protein.P37639]] `RegulonDB` `S` - regulator=GadX; target=murI; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012989,ECOCYC:EG11204,GeneID:948467`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4165428-4166285:+; feature_type=gene
