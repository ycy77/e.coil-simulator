---
entity_id: "gene.b1050"
entity_type: "gene"
name: "yceK"
source_database: "NCBI RefSeq"
source_id: "gene-b1050"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1050"
  - "yceK"
---

# yceK

`gene.b1050`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1050`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yceK (gene.b1050) is a gene entity. It encodes yceK (protein.P0AB31). Encoded protein function: Uncharacterized protein YceK EcoCyc product frame: EG12689-MONOMER. Genomic coordinates: 1113579-1113806. EcoCyc protein note: Strong aggravating genetic interactions (measured by relative colony size and fitness in rich medium) were observed between lptD and yceK . Deletion of yceK results in impaired outer membrane integrity as evidenced by vancomycin-induced morphological defects and lowered outer membrane protein (OMP) abundance . Deletion of yceK and lptD results in cell wall failure/lysis, lowered OMP abundance and increased levels of the DegP stress response protease . Overexpression of yceK suppresses the essentiality of EG12691-MONOMER lapB, which encodes a protein involved in lipopolysaccharide (LPS) assembly. The defects in LPS composition that occur in a Δ(lapA lapB) mutant are exacerbated in a Δ(lapA lapB yceK) mutant . yceK contains a predicted lipoprotein signal . YceK is a verified lipoprotein according to unpublished data by S. Matsuyama et al. (cited in ).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AB31|protein.P0AB31]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003565,ECOCYC:EG12689,GeneID:945613`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1113579-1113806:+; feature_type=gene
