---
entity_id: "gene.b2232"
entity_type: "gene"
name: "ubiG"
source_database: "NCBI RefSeq"
source_id: "gene-b2232"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2232"
  - "ubiG"
---

# ubiG

`gene.b2232`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2232`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ubiG (gene.b2232) is a gene entity. It encodes ubiG (protein.P17993). Encoded protein function: FUNCTION: O-methyltransferase that catalyzes the 2 O-methylation steps in the ubiquinone biosynthetic pathway. {ECO:0000255|HAMAP-Rule:MF_00472, ECO:0000269|PubMed:10419476}. EcoCyc product frame: DHHB-METHYLTRANSFER-MONOMER. EcoCyc synonyms: pufX, yfaB. Genomic coordinates: 2339567-2340289. EcoCyc protein note: UbiG is an S-adenosyl-L-methionine (SAM)-dependent O-methyltransferase that catalyzes both O-methylation reactions in the biosynthesis of ubiquinone and is a component of the Ubi complex metabolon . The enzyme is mostly cytoplasmic, but also shows some association with the membrane . Purified UbiG binds to liposomes, with preferences for phosphatidylglycerol and cardiolipin . Crystal structures of wild-type and mutant UbiG in complex with S-adenosyl-L-homocysteine (SAH) have been determined . A unique, conserved membrane-binding region was identified and its function confirmed by mutating amino acid residues within this region . Interaction of this region with the cytoplasmic membrane may open a channel that provides access for SAM to its binding site . Liposome-associated UbiG has ~11-fold increased affinity for SAH . However, whether or not the membrane association of UbiG contributes to its catalytic activity has not yet been investigated...

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P17993|protein.P17993]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007374,ECOCYC:EG11143,GeneID:946607`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2339567-2340289:+; feature_type=gene
