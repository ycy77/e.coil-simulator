---
entity_id: "gene.b1613"
entity_type: "gene"
name: "manA"
source_database: "NCBI RefSeq"
source_id: "gene-b1613"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1613"
  - "manA"
---

# manA

`gene.b1613`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1613`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

manA (gene.b1613) is a gene entity. It encodes manA (protein.P00946). Encoded protein function: FUNCTION: Involved in the conversion of glucose to GDP-L-fucose, which can be converted to L-fucose, a capsular polysaccharide. EcoCyc product frame: MANNPISOM-MONOMER. EcoCyc synonyms: pmi. Genomic coordinates: 1688576-1689751. EcoCyc protein note: Mannose-6-phosphate isomerase (phosphomannose isomerase, PMI) catalyzes the reversible isomerization of mannose-6-phosphate and fructose-6-phosphate. This reaction is the first committed step in the synthesis of GDP-α-D-mannose (see pathway PWY-5659). The enzyme is required for growth on mannose as the sole source of carbon and energy. It is also required for the formation of GDP-L-fucose, a building block of capsular polysaccharide (see pathways MANNCAT-PWY and COLANSYN-PWY). PMI activity is increased by growth on p-fluorophenylalanine (FPA), which leads to formation of mucoid colonies . A manA mutant is unable to grow on mannose as the sole source of carbon and energy and has a defect in the maintenance of colonization of the mouse intestine . The manA gene can be used as a selectable marker . Pmi: "phosphomannose isomerase" The E. coli enzyme is a type I PMI, a monofunctional, Zn2+-dependent metalloenzyme found in most bacteria and mammals...

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579), arcA (protein.P0A9Q1).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00946|protein.P00946]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=manA; function=+
- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=manA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005398,ECOCYC:EG10566,GeneID:944840`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1688576-1689751:+; feature_type=gene
