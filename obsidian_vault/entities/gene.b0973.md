---
entity_id: "gene.b0973"
entity_type: "gene"
name: "hyaB"
source_database: "NCBI RefSeq"
source_id: "gene-b0973"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0973"
  - "hyaB"
---

# hyaB

`gene.b0973`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0973`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hyaB (gene.b0973) is a gene entity. It encodes hyaB (protein.P0ACD8). Encoded protein function: FUNCTION: This is one of three E.coli hydrogenases synthesized in response to different physiological conditions. HYD1 is believed to have a role in hydrogen cycling during fermentative growth. EcoCyc product frame: HYAB-MONOMER. Genomic coordinates: 1033254-1035047. EcoCyc protein note: HyaB is the large subunit of hydrogenase 1 and contains the Ni-Fe active site. The nickel and iron atoms are coordinated by 4 Cys thiolates plus 3 diatomic ligands (2 cyano and a carbonyl). Acquisition of the [NiFe] cofactor, C-terminal processing of HyaB and subsequent association with the small subunit (HyaA) are required prior to export by the Tat system (and reviewed in . A hyaB in-frame deletion mutant does not have a defect in anaerobic growth with hydrogen and fumarate as sole energy and carbon sources; a hyaB hybC double mutant does not grow under these conditions .

## Biological Role

Repressed by iscR (protein.P0AGK8). Activated by ydeO (protein.P76135).

## Enriched Pathways

- `eco00633` Nitrotoluene degradation (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACD8|protein.P0ACD8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P76135|protein.P76135]] `RegulonDB` `S` - regulator=YdeO; target=hyaB; function=+
- `represses` <-- [[protein.P0AGK8|protein.P0AGK8]] `RegulonDB` `S` - regulator=IscR; target=hyaB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003288,ECOCYC:EG10469,GeneID:945580`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1033254-1035047:+; feature_type=gene
