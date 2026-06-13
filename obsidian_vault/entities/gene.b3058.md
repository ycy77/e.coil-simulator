---
entity_id: "gene.b3058"
entity_type: "gene"
name: "folB"
source_database: "NCBI RefSeq"
source_id: "gene-b3058"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3058"
  - "folB"
---

# folB

`gene.b3058`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3058`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

folB (gene.b3058) is a gene entity. It encodes folB (protein.P0AC16). Encoded protein function: FUNCTION: Catalyzes the conversion of 7,8-dihydroneopterin to 6-hydroxymethyl-7,8-dihydropterin. Can use L-threo-dihydroneopterin and D-erythro-dihydroneopterin as substrates for the formation of 6-hydroxymethyldihydropterin, but it can also catalyze the epimerization of carbon 2' of dihydroneopterin to dihydromonapterin at appreciable velocity. {ECO:0000269|PubMed:9651328}. EcoCyc product frame: H2NEOPTERINALDOL-MONOMER. EcoCyc synonyms: ygiG. Genomic coordinates: 3204221-3204589. EcoCyc protein note: Dihydroneopterin aldolase (FolB) is an enzyme in the folate biosynthesis pathway, an important antibacterial drug target. The reaction mechanism has been investigated. The conserved Y53 residue is important for the aldolase reaction . Site-directed mutagenesis of conserved active site residues suggested that E22 is important for substrate binding, but not catalysis, and that E21 and K98 are important for both substrate binding and catalysis . Unlike other aldolase-catalyzed reactions, the dihydroneopterin aldolase reaction was initially found to be irreversible . However, with an enzyme preparation of higher activity and a higher glycolaldehyde concentration, the reaction catalyzed by the Staphylococcus aureus enzyme is readily reversible...

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AC16|protein.P0AC16]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010036,ECOCYC:EG11673,GeneID:947544`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3204221-3204589:-; feature_type=gene
