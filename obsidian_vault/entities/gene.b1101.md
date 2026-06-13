---
entity_id: "gene.b1101"
entity_type: "gene"
name: "ptsG"
source_database: "NCBI RefSeq"
source_id: "gene-b1101"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1101"
  - "ptsG"
---

# ptsG

`gene.b1101`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1101`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ptsG (gene.b1101) is a gene entity. It encodes ptsG (protein.P69786). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II complex composed of PtsG and Crr is involved in glucose transport (PubMed:10562420, PubMed:3129430). Also functions as a chemoreceptor monitoring the environment for changes in sugar concentration and an effector modulating the activity of the transcriptional repressor Mlc (PubMed:18319344). In the presence of glucose in the medium, the dephosphorylated form of PtsG can interact with Mlc, leading to sequestration of Mlc in the inner membrane and inhibition of its repressor activity (PubMed:11032803, PubMed:11157755, PubMed:12529317, PubMed:18319344). {ECO:0000269|PubMed:10562420, ECO:0000269|PubMed:11032803, ECO:0000269|PubMed:11157755, ECO:0000269|PubMed:12529317, ECO:0000269|PubMed:18319344, ECO:0000269|PubMed:3129430}.; FUNCTION: (Microbial infection) Probably transports the toxic C-terminal region of CdiA from E.coli strains NC101 and 3006 across the inner membrane to the cytoplasm, where CdiA degrades specific tRNAs...

## Biological Role

Repressed by sgrS (gene.b4577), fis (protein.P0A6R3), arcA (protein.P0A9Q1), mlc (protein.P50456). Activated by rpoD (protein.P00579), fis (protein.P0A6R3), soxS (protein.P0A9E2), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69786|protein.P69786]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (8)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ptsG; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=ptsG; function=-+
- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `S` - regulator=SoxS; target=ptsG; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=ptsG; function=+
- `represses` <-- [[gene.b4577|gene.b4577]] `RegulonDB` `S` - regulator=SgrS; target=ptsG; function=-
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=ptsG; function=-+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=ptsG; function=-
- `represses` <-- [[protein.P50456|protein.P50456]] `RegulonDB` `S` - regulator=Mlc; target=ptsG; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003722,ECOCYC:EG10787,GeneID:945651`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1157869-1159302:+; feature_type=gene
