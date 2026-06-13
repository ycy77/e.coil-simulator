---
entity_id: "gene.b0421"
entity_type: "gene"
name: "ispA"
source_database: "NCBI RefSeq"
source_id: "gene-b0421"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0421"
  - "ispA"
---

# ispA

`gene.b0421`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0421`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ispA (gene.b0421) is a gene entity. It encodes ispA (protein.P22939). Encoded protein function: Farnesyl diphosphate synthase (FPP synthase) (EC 2.5.1.10) ((2E,6E)-farnesyl diphosphate synthase) (Geranyltranstransferase) EcoCyc product frame: FPPSYN-MONOMER. Genomic coordinates: 440202-441101. EcoCyc protein note: Farnesyl diphosphate synthase can utilize both prenyl (dimethylallyl) and geranyl diphosphates as substrates, generating geranyl and farnesyl diphosphate, respectively. Therefore the enzyme can catalyze two sequential reactions in the polyisoprenoid biosynthetic pathway . Isoprenoid product chain length specificity determinants within IspA were identified by random PCR mutagenesis . Substrate selectivity and stereoselectivity of the enzyme have been investigated . Crystal structures of ternary complexes of the enzyme with substrate(s) or an inhibitor have been solved, revealing the contribution of three Mg2+ ions to substrate binding and catalysis . Even though ispA has been reported to be essential for growth , ispA null mutants are viable, with near-wild type growth yield under anaerobic conditions and a slight reduction in growth yield under aerobic conditions. The mutant contains less than 13% and 18%, respectively, of ubiquinone-8 and menaquinone-8 and 40-70% of the wild-type levels of undecaprenyl phosphate...

## Enriched Pathways

- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P22939|protein.P22939]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001463,ECOCYC:EG10508,GeneID:945064`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:440202-441101:-; feature_type=gene
