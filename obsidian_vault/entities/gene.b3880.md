---
entity_id: "gene.b3880"
entity_type: "gene"
name: "yihS"
source_database: "NCBI RefSeq"
source_id: "gene-b3880"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3880"
  - "yihS"
---

# yihS

`gene.b3880`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3880`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yihS (gene.b3880) is a gene entity. It encodes yihS (protein.P32140). Encoded protein function: FUNCTION: Catalyzes the isomerization of sulfoquinovose (SQ) to 6-deoxy-6-sulfo-D-fructose (SF) (PubMed:24463506, PubMed:33791429). Can also catalyze the interconversion of SQ and sulforhamnose (SR) (PubMed:33791429). Has a clear preference for beta-SQ and little-to-no activity on alpha-SQ (PubMed:33791429). In vitro, can also catalyze the interconversion of mannose, fructose and glucose, or lyxose and xylulose, but has extremely low activity with glucose (PubMed:18328504). {ECO:0000269|PubMed:18328504, ECO:0000269|PubMed:24463506, ECO:0000269|PubMed:33791429}. EcoCyc product frame: EG11845-MONOMER. EcoCyc synonyms: squS. Genomic coordinates: 4070515-4071756. EcoCyc protein note: Sulfoquinovose isomerase (YihS) catalyzes the isomerization to CPD-16501 , a part of the PWY-7446 pathway. YihS has mannose isomerase activity in vitro. Predicted active site residues were analyzed by site-directed mutagenesis. A crystal structure of the enzyme has been solved at 2.5 Å resolution . YihS may be identical to the enzyme first identified by , although the quarternary structure differs. The mannose isomerase identified in is a tetramer in solution, while YihS is a hexamer . Expression of YihS is induced by growth on sulfoquinovose and lactose...

## Biological Role

Repressed by csqR (protein.P32144). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00566` Sulfoquinovose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32140|protein.P32140]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yihS; function=+
- `represses` <-- [[protein.P32144|protein.P32144]] `RegulonDB` `S` - regulator=CsqR; target=yihS; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012673,ECOCYC:EG11845,GeneID:948374`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4070515-4071756:-; feature_type=gene
