---
entity_id: "gene.b4112"
entity_type: "gene"
name: "basS"
source_database: "NCBI RefSeq"
source_id: "gene-b4112"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4112"
  - "basS"
---

# basS

`gene.b4112`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4112`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

basS (gene.b4112) is a gene entity. It encodes basS (protein.P30844). Encoded protein function: FUNCTION: Member of the two-component regulatory system BasS/BasR Autophosphorylates and activates BasR by phosphorylation. {ECO:0000269|PubMed:15522865}. EcoCyc product frame: PHOSPHO-BASS. EcoCyc synonyms: pmrB, dgkR. Genomic coordinates: 4332181-4333272. EcoCyc protein note: BasS (also known as PmrB) is the sensor histidine kinase of the BasSR two-component system. BasS is a predicted integral membrane protein with sequence similarity to the sensor kinase family of proteins including a conserved histidine (His-152) which is presumed to be the site of autophosphorylation; overproduced BasS autophosphorylates in the presence of ATP and transfers a phosphate to its cognate response regulator, BasR in vitro; it is also able to phosphorylate purified OmpR with low efficiency (see also ). The purified cytoplasmic domain of BasS (Arg-89 → Ile-363) has phospho-BasR phosphatase activity in vitro; variation in the protein phosphatase activity of BasS (PmrB) between E. coli and Salmonella enterica determines the ability of G7172-MONOMER "PmrD" to activate the BasSR (PmrAB) system in the two species . BasSR is required for the Fe(III)-dependent induction of the arnBCADTEF operon; a ΔbasSR strain exhibits mild acid-sensitivity when grown aerobically in medium containing a high (1...

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30844|protein.P30844]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013464,ECOCYC:EG11614,GeneID:948632`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4332181-4333272:-; feature_type=gene
