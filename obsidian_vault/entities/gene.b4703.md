---
entity_id: "gene.b4703"
entity_type: "gene"
name: "pmrR"
source_database: "NCBI RefSeq"
source_id: "gene-b4703"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4703"
  - "pmrR"
---

# pmrR

`gene.b4703`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4703`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pmrR (gene.b4703) is a gene entity. It encodes pmrR (protein.G3MTW7). Encoded protein function: FUNCTION: May bind to BasS and modulate its sensor kinase activity. {ECO:0000305}. EcoCyc product frame: MONOMER0-4214. Genomic coordinates: 4332116-4332205. EcoCyc protein note: First characterized in TAX-90371 , pmrR encodes a small inner membrane protein which, under BasSR-inducing conditions (high concentrations of Fe3+, mildly acidic pH), inhibits the G7146-MONOMER LpxT-dependent generation of lipid A-core 1-diphosphate . Inactivation of pmrR in the polymyxin-resistant, deoxycholate-sensitive EG11615 BasR(PmrA)-constitutive strain WD101 results in sensitivity to polymyxin B and resistance to deoxycholate . PmrR-mediated regulation of LpxT activity in Salmonella, constitutes a negative feedback mechanism for control of the PmrA-PmrB two-component system which governs transcription of lipopolysaccharide-modifying genes .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.G3MTW7|protein.G3MTW7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ECOCYC:G0-10707,GeneID:11115379`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4332116-4332205:+; feature_type=gene
