---
entity_id: "gene.b2904"
entity_type: "gene"
name: "gcvH"
source_database: "NCBI RefSeq"
source_id: "gene-b2904"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2904"
  - "gcvH"
---

# gcvH

`gene.b2904`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2904`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gcvH (gene.b2904) is a gene entity. It encodes gcvH (protein.P0A6T9). Encoded protein function: FUNCTION: The glycine cleavage system catalyzes the degradation of glycine. The H protein shuttles the methylamine group of glycine from the P protein to the T protein. {ECO:0000255|HAMAP-Rule:MF_00272, ECO:0000269|PubMed:8375392}. EcoCyc product frame: LIPOYL-GCVH. EcoCyc synonyms: gcv. Genomic coordinates: 3049160-3049549. EcoCyc protein note: The H-protein, coded for by the gcvH gene, is a lipoylprotein that is reduced as it shuttles the methylamine group of glycine from the P-protein to the T-protein and is reoxidized by the dihydrolipoamide dehydrogenase. GcvH functions as a substrate for the three enzymes of the gcv complex. Residues 61-65 are predicted to contain the lipoyl modification (on lysine), based on conservation of these residues and their correspondence to the lipoate attachment site of the Pisum sativum protein . The interaction between GcvH and GcvT has been examined . Interaction between the two proteins may be necessary to form the folate binding site, in which the folate polyglutamyl region binds, exposing the pteridine ring . The GcvT N terminus is important for interaction with GcvH, probably by mediating a conformational change, and residue D43 of GcvH is proximal to GcvT in the GcvH-GcvT complex...

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

- `encodes` --> [[protein.P0A6T9|protein.P0A6T9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gcvH; function=+
- `activates` <-- [[protein.P0A9F6|protein.P0A9F6]] `RegulonDB` `C` - regulator=GcvA; target=gcvH; function=-+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=gcvH; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=gcvH; function=+
- `represses` <-- [[protein.P0A9F6|protein.P0A9F6]] `RegulonDB` `C` - regulator=GcvA; target=gcvH; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0009534,ECOCYC:EG10371,GeneID:947393`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3049160-3049549:-; feature_type=gene
