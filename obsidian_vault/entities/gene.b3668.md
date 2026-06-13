---
entity_id: "gene.b3668"
entity_type: "gene"
name: "uhpB"
source_database: "NCBI RefSeq"
source_id: "gene-b3668"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3668"
  - "uhpB"
---

# uhpB

`gene.b3668`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3668`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

uhpB (gene.b3668) is a gene entity. It encodes uhpB (protein.P09835). Encoded protein function: FUNCTION: Part of the UhpABC signaling cascade that controls the expression of the hexose phosphate transporter UhpT. UhpB functions as a membrane-associated protein kinase that autophosphorylates in response to interaction with UhpC, and subsequently transfers its phosphate group to the response regulator UhpA (PubMed:11053370, PubMed:11739766, PubMed:3038843, PubMed:8349544). Can also dephosphorylate UhpA (PubMed:11053370, PubMed:11739766). {ECO:0000269|PubMed:11053370, ECO:0000269|PubMed:11739766, ECO:0000269|PubMed:3038843, ECO:0000269|PubMed:8349544}. EcoCyc product frame: PHOSPHO-UHPB. Genomic coordinates: 3848634-3850136. EcoCyc protein note: This is the phosphorylated form of UHPB-MONOMER UhpB - the sensor histidine kinase of the UhpBA two-component signal transduction system. EcoCyc protein note: UhpB belongs to the phosphorelay system UhpB-UhpC-UhpA which is involved in the regulation of the uptake of hexose phosphates. UhpB is a membrane bound histidine kinase with eight predicted transmembrane helices and a C-terminal cytoplasmic domain containing the characteristic histidine kinase sequence motifs . UhpB autophosphorylates on a conserved histidine residue (His313) and transfers the phosphoryl group its cognate response regulator, UhpA...

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P09835|protein.P09835]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011993,ECOCYC:EG11052,GeneID:948195`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3848634-3850136:-; feature_type=gene
