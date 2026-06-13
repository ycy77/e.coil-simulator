---
entity_id: "gene.b0974"
entity_type: "gene"
name: "hyaC"
source_database: "NCBI RefSeq"
source_id: "gene-b0974"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0974"
  - "hyaC"
---

# hyaC

`gene.b0974`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0974`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hyaC (gene.b0974) is a gene entity. It encodes hyaC (protein.P0AAM1). Encoded protein function: FUNCTION: Probable b-type cytochrome. EcoCyc product frame: HYAC-MONOMER. EcoCyc synonyms: cybH. Genomic coordinates: 1035066-1035773. EcoCyc protein note: The hyaC gene product is very hydrophobic, rich in aromatic residues, and has four putative hydrophobic membrane-spanning regions . An in-frame deletion in the hyaC gene results in wild-type levels of hydrogenase 1 activity and the appearance of multiple forms of the enzyme during purification . Sequence analysis suggests that the HyaC subunit contains two heme groups but only one heme could be identified in the crystal structure of the hydrogenase 1 complex; HyaC's main function may be anchoring the hydrogenase to the membrane . Overexpression of hyaC from an ASKA plasmid leads to a more than 3-fold increase in the MIC of hypochlorous acid .

## Biological Role

Repressed by iscR (protein.P0AGK8). Activated by arcA (protein.P0A9Q1), ydeO (protein.P76135).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAM1|protein.P0AAM1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=hyaC; function=+
- `activates` <-- [[protein.P76135|protein.P76135]] `RegulonDB` `S` - regulator=YdeO; target=hyaC; function=+
- `represses` <-- [[protein.P0AGK8|protein.P0AGK8]] `RegulonDB` `S` - regulator=IscR; target=hyaC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003290,ECOCYC:EG10470,GeneID:945581`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1035066-1035773:+; feature_type=gene
