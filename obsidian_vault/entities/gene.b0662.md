---
entity_id: "gene.b0662"
entity_type: "gene"
name: "ubiF"
source_database: "NCBI RefSeq"
source_id: "gene-b0662"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0662"
  - "ubiF"
---

# ubiF

`gene.b0662`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0662`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ubiF (gene.b0662) is a gene entity. It encodes ubiF (protein.P75728). Encoded protein function: FUNCTION: Catalyzes the hydroxylation of 2-octaprenyl-3-methyl-6-methoxy-1,4-benzoquinol during ubiquinone biosynthesis. {ECO:0000269|PubMed:10802164}. EcoCyc product frame: OCTAPRENYL-METHYL-METHOXY-BENZOQ-OH-MON. EcoCyc synonyms: yleB. Genomic coordinates: 695101-696276. EcoCyc protein note: 2-Octaprenyl-3-methyl-6-methoxy-1,4-benzoquinol hydroxylase catalyzes the hydroxylation of C-5 of the benzene moiety in the biosynthesis of ubiquinone. The enzyme has not been characterized biochemically. UbiF is a component of the Ubi complex metabolon . UbiF predominantly localizes to the cytosol. The seven ubiquinone biosynthesis proteins UbiE, UbiF, UbiG, UbiH, UbiI, UbiJ, and UbiK form a 1 MDa complex in the cytosol . A ubiF mutant accumulates 2-octaprenyl-3-methyl-6-methoxy-1,4-benzoquinone (MMQ-8) and has only a slight growth defect . MMQ-8 itself can function fairly efficiently (~50%) as an electron carrier in the NADH, D-lactate, and glycerol-3-phosphate dehydrogenase systems, but only poorly for the oxidation of succinate . A ubiF mutant is unable to grow on succinate as the sole source of carbon and energy . ubiF mutants have reduced capacity for uptake of aminoglycoside antibiotics and are resistant to phleomycin, bleomycin, and heat inactivation...

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75728|protein.P75728]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002265,ECOCYC:G6365,GeneID:945261`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:695101-696276:+; feature_type=gene
