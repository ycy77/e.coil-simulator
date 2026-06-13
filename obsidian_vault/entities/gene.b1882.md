---
entity_id: "gene.b1882"
entity_type: "gene"
name: "cheY"
source_database: "NCBI RefSeq"
source_id: "gene-b1882"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1882"
  - "cheY"
---

# cheY

`gene.b1882`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1882`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cheY (gene.b1882) is a gene entity. It encodes cheY (protein.P0AE67). Encoded protein function: FUNCTION: Involved in the transmission of sensory signals from the chemoreceptors to the flagellar motors. In its active (phosphorylated or acetylated) form, CheY exhibits enhanced binding to a switch component, FliM, at the flagellar motor which induces a change from counterclockwise to clockwise flagellar rotation. Overexpression of CheY in association with MotA and MotB improves motility of a ycgR disruption, suggesting there is an interaction (direct or indirect) between the c-di-GMP-binding flagellar brake protein and the flagellar stator. {ECO:0000269|PubMed:20346719}. EcoCyc product frame: MONOMER0-4170. Genomic coordinates: 1967048-1967437. EcoCyc protein note: CheY is one of two response regulators in chemotactic two component signaling pathways. CheY undergoes two covalent modifications - phosphorylation and acetylation - both modifications influence CheY's interaction with the cognate sensor kinase CHEA-CPLX "CheA", the switch protein and target at the flagellar complex, FLIM-FLAGELLAR-C-RING-SWITCH "FliM" and the phosphatase CHEZ-CPLX "CheZ". CheY is reversibly phosphorylated (at aspartate residue 57) by the sensor histidine kinase CheA . CheY-phosphate is inherently unstable; CheZ accelerates its dephosphorylation (see also )...

## Biological Role

Activated by fliA (protein.P0AEM6).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE67|protein.P0AE67]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AEM6|protein.P0AEM6]] `RegulonDB` `S` - sigma=sigma28; target=cheY; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006280,ECOCYC:EG10150,GeneID:946393`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1967048-1967437:-; feature_type=gene
