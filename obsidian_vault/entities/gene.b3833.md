---
entity_id: "gene.b3833"
entity_type: "gene"
name: "ubiE"
source_database: "NCBI RefSeq"
source_id: "gene-b3833"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3833"
  - "ubiE"
---

# ubiE

`gene.b3833`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3833`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ubiE (gene.b3833) is a gene entity. It encodes ubiE (protein.P0A887). Encoded protein function: FUNCTION: Methyltransferase required for the conversion of demethylmenaquinol (DMKH2) to menaquinol (MKH2) and the conversion of 2-polyprenyl-6-methoxy-1,4-benzoquinol (DDMQH2) to 2-polyprenyl-3-methyl-6-methoxy-1,4-benzoquinol (DMQH2) (PubMed:9045837). In vitro, can use demethylphylloquinol, an intermediate in the biosynthesis of phylloquinone (vitamin K1) in plants and cyanobacteria (PubMed:26023160). {ECO:0000269|PubMed:26023160, ECO:0000269|PubMed:9045837}. EcoCyc product frame: 2-OCTAPRENYL-METHOXY-BENZOQ-METH-MONOMER. EcoCyc synonyms: yigO. Genomic coordinates: 4018855-4019610. EcoCyc protein note: UbiE is a C-methyltransferase that catalyzes reactions in both ubiquinone (Q) and menaquinone (MK) biosynthesis. Q biosynthesis and MK biosynthesis diverge after the formation of chorismate and the pathways proceed independently except for the C methylation step. In Q biosynthesis, UbiE catalyzes the conversion of 2-octaprenyl-6-methoxy-1,4-benzoquinone to 2-octaprenyl-3-methyl-6-methoxy-1,4-benzoquinone. In MK biosynthesis, UbiE catalyzes the conversion of demethylmenaquinone to menaquinone . UbiE localizes to both soluble and membrane fractions. The seven ubiquinone biosynthesis proteins UbiE, UbiF, UbiG, UbiH, UbiI, UbiJ, and UbiK form a 1 MDa complex in the cytosol...

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A887|protein.P0A887]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012534,ECOCYC:EG11473,GeneID:948926`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4018855-4019610:+; feature_type=gene
