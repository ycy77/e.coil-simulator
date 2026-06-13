---
entity_id: "gene.b2903"
entity_type: "gene"
name: "gcvP"
source_database: "NCBI RefSeq"
source_id: "gene-b2903"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2903"
  - "gcvP"
---

# gcvP

`gene.b2903`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2903`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gcvP (gene.b2903) is a gene entity. It encodes gcvP (protein.P33195). Encoded protein function: FUNCTION: The glycine cleavage system catalyzes the degradation of glycine. The P protein binds the alpha-amino group of glycine through its pyridoxal phosphate cofactor; CO(2) is released and the remaining methylamine moiety is then transferred to the lipoamide cofactor of the H protein. {ECO:0000255|HAMAP-Rule:MF_00711, ECO:0000269|PubMed:8375392}. EcoCyc product frame: GCVP-MONOMER. Genomic coordinates: 3046168-3049041. EcoCyc protein note: Together with GcvH, GcvT and E3 (Lpd), GcvP forms a loosely associated complex known as the glycine cleavage system. GcvP, also known as the P-protein, catalyzes the decarboxylation of glycine. The remaining aminomethyl moiety is transferred to the lipoyl prosthetic group of the H-protein . Glycine cleavage system mutations cause a defect in utilization of glycine to form serine . Expression of the glycine cleavage enzyme system is induced by glycine , and the transcriptional regulation of the gcvTHP operon has been studied extensively. E. coli BW25113 strains with deletions in gcvP or EG11795 can grow in minimal media M9 when 0.5 M SARCOSINE is present but not in 0.75 M sarcosine . Review: Module 3.6.1.2

## Biological Role

Repressed by gcvA (protein.P0A9F6). Activated by rpoD (protein.P00579), gcvA (protein.P0A9F6), lrp (protein.P0ACJ0), crp (protein.P0ACJ8).

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

- `encodes` --> [[protein.P33195|protein.P33195]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gcvP; function=+
- `activates` <-- [[protein.P0A9F6|protein.P0A9F6]] `RegulonDB` `C` - regulator=GcvA; target=gcvP; function=-+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=gcvP; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=gcvP; function=+
- `represses` <-- [[protein.P0A9F6|protein.P0A9F6]] `RegulonDB` `C` - regulator=GcvA; target=gcvP; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0009531,ECOCYC:EG11810,GeneID:947394`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3046168-3049041:-; feature_type=gene
