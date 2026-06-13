---
entity_id: "gene.b1324"
entity_type: "gene"
name: "tpx"
source_database: "NCBI RefSeq"
source_id: "gene-b1324"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1324"
  - "tpx"
---

# tpx

`gene.b1324`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1324`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tpx (gene.b1324) is a gene entity. It encodes tpx (protein.P0A862). Encoded protein function: FUNCTION: Thiol-specific peroxidase that catalyzes the reduction of hydrogen peroxide and organic hydroperoxides to water and alcohols, respectively. Plays a role in cell protection against oxidative stress by detoxifying peroxides. Has a preference for alkyl hydroperoxides and acts as a lipid peroxidase to inhibit bacterial membrane oxidation. Acts as a principal antioxidant during anaerobic growth. {ECO:0000255|HAMAP-Rule:MF_00269, ECO:0000269|PubMed:12514184, ECO:0000269|PubMed:14676195}. EcoCyc product frame: G6660-MONOMER. EcoCyc synonyms: yzzJ. Genomic coordinates: 1388305-1388811. EcoCyc protein note: Tpx is a RED-THIOREDOXIN-MONOMER-dependent thiol peroxidase that belongs to the family of atypical 2-Cys peroxidases . In vivo, Tpx appears to function as a lipid hydroperoxide peroxidase and acts as the principal antioxidant under anaerobic conditions . Osmotic shock experiments initially indicated that the enzyme was located in the periplasm . However, no signal sequence for transport into the periplasm is evident, and in vivo interaction with RED-THIOREDOXIN-MONOMER indicates that the enzyme is located in the cytoplasm . Kinetic analysis shows a bisubstrate ping-pong catalytic mechanism...

## Biological Role

Repressed by arcA (protein.P0A9Q1). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A862|protein.P0A862]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=tpx; function=+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=tpx; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004442,ECOCYC:G6660,GeneID:945880`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1388305-1388811:-; feature_type=gene
