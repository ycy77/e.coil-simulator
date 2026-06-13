---
entity_id: "gene.b3930"
entity_type: "gene"
name: "menA"
source_database: "NCBI RefSeq"
source_id: "gene-b3930"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3930"
  - "menA"
---

# menA

`gene.b3930`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3930`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

menA (gene.b3930) is a gene entity. It encodes menA (protein.P32166). Encoded protein function: FUNCTION: Conversion of 1,4-dihydroxy-2-naphthoate (DHNA) to demethylmenaquinone (DMK). Attaches octaprenylpyrophosphate, a membrane-bound 40-carbon side chain to DHNA. The conversion of DHNA to DMK proceeds in three stages: the removal of the carboxyl group of DHNA as CO(2), the attachment of the isoprenoid side chain, and a quinol-to-quinone oxidation, which is thought to be spontaneous. {ECO:0000269|PubMed:9573170}. EcoCyc product frame: DMK-MONOMER. EcoCyc synonyms: yiiW. Genomic coordinates: 4119423-4120349. EcoCyc protein note: 1,4-dihydroxy-2-naphthoate octaprenyltransferase (MenA) catalyzes the transfer of an octaprenyl side chain to DHNA, the reaction in menaquinone biosynthesis where the pathway becomes associated with the membrane . Site-directed mutagenesis of predicted active site residues confirmed their importance for catalytic activity. A reaction mechanism has been proposed . MenA is an inner membrane protein with nine predicted transmembrane domains. The C-terminus is located in the periplasm . A menA mutant accumulates 1,4-dihydroxy-2-naphthoate in the culture supernatant . menA transposon insertion mutants have increased resistance to the plant essential oils thymol and menthol . Review:

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32166|protein.P32166]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012841,ECOCYC:EG11880,GeneID:948418`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4119423-4120349:-; feature_type=gene
