---
entity_id: "gene.b3052"
entity_type: "gene"
name: "hldE"
source_database: "NCBI RefSeq"
source_id: "gene-b3052"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3052"
  - "hldE"
---

# hldE

`gene.b3052`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3052`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hldE (gene.b3052) is a gene entity. It encodes hldE (protein.P76658). Encoded protein function: FUNCTION: Catalyzes the phosphorylation of D-glycero-D-manno-heptose 7-phosphate at the C-1 position to selectively form D-glycero-beta-D-manno-heptose-1,7-bisphosphate. {ECO:0000269|PubMed:11751812}.; FUNCTION: Catalyzes the ADP transfer from ATP to D-glycero-beta-D-manno-heptose 1-phosphate, yielding ADP-D-glycero-beta-D-manno-heptose. {ECO:0000269|PubMed:11751812}. EcoCyc product frame: G7590-MONOMER. EcoCyc synonyms: yqiF, rfaE, gmhC, waaE. Genomic coordinates: 3195320-3196753. EcoCyc protein note: HldE catalyzes two reactions in the PWY0-1241 pathway, which provides one of the building blocks for the inner core region of lipopolysaccharide (LPS) . The bifunctionality of HldE results from a fusion of an N-terminal ribokinase superfamily domain and a C-terminal cytidylyltransferase superfamily domain; the two domains are genetically and physically separable . Structural modelling of the ribokinase domain led to the identification of amino acid residues potentially essential for catalysis. Site-directed mutagenesis of potential ATP binding site residues resulted in a dominant negative mutant phenotype . In a genetic screen for heptoseless mutants, a transposon insertion in the hldE gene was identified...

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76658|protein.P76658]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010015,ECOCYC:G7590,GeneID:947548`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3195320-3196753:-; feature_type=gene
