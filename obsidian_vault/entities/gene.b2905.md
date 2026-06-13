---
entity_id: "gene.b2905"
entity_type: "gene"
name: "gcvT"
source_database: "NCBI RefSeq"
source_id: "gene-b2905"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2905"
  - "gcvT"
---

# gcvT

`gene.b2905`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2905`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gcvT (gene.b2905) is a gene entity. It encodes gcvT (protein.P27248). Encoded protein function: FUNCTION: The glycine cleavage system catalyzes the degradation of glycine. {ECO:0000255|HAMAP-Rule:MF_00259, ECO:0000269|PubMed:8375392}. EcoCyc product frame: GCVT-MONOMER. Genomic coordinates: 3049573-3050667. EcoCyc protein note: Together with GcvH, GcvP and E3 (Lpd), GvcT forms a loosely associated complex known as the glycine cleavage system. GvcT, also known as the T-protein, catalyzes the release of ammonia from the intermediate attached to the H-protein and the synthesis of methylenetetrahydrofolate in the presence of tetrahydrofolate . Residues involved in binding of folate have been identified by crosslinking and site-directed mutagenesis . The N-terminal region of GvcT is important for the proper conformation of GvcT, allowing interaction with the H-protein . Glycine cleavage system mutations cause a defect in utilization of glycine to form serine . Expression of the glycine cleavage enzyme system is induced by glycine , and the transcriptional regulation of the gcvTHP operon has been studied extensively. Review: Module 3.6.1.2

## Biological Role

Repressed by gcvA (protein.P0A9F6), lrp (protein.P0ACJ0), nac (protein.Q47005). Activated by rpoD (protein.P00579), gcvA (protein.P0A9F6), lrp (protein.P0ACJ0), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27248|protein.P27248]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gcvT; function=+
- `activates` <-- [[protein.P0A9F6|protein.P0A9F6]] `RegulonDB` `C` - regulator=GcvA; target=gcvT; function=-+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=gcvT; function=-+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=gcvT; function=+
- `represses` <-- [[protein.P0A9F6|protein.P0A9F6]] `RegulonDB` `C` - regulator=GcvA; target=gcvT; function=-+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=gcvT; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=gcvT; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009536,ECOCYC:EG11442,GeneID:947390`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3049573-3050667:-; feature_type=gene
