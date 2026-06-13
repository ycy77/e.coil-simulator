---
entity_id: "gene.b0605"
entity_type: "gene"
name: "ahpC"
source_database: "NCBI RefSeq"
source_id: "gene-b0605"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0605"
  - "ahpC"
---

# ahpC

`gene.b0605`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0605`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ahpC (gene.b0605) is a gene entity. It encodes ahpC (protein.P0AE08). Encoded protein function: FUNCTION: Thiol-specific peroxidase that catalyzes the reduction of hydrogen peroxide and organic hydroperoxides to water and alcohols, respectively. Plays a role in cell protection against oxidative stress by detoxifying peroxides. Is the primary scavenger for endogenously generated hydrogen peroxides. {ECO:0000269|PubMed:11717276}. EcoCyc product frame: EG11384-MONOMER. EcoCyc synonyms: tpx, ssi8. Genomic coordinates: 638945-639508. EcoCyc protein note: AhpC is the peroxidase component of alkyl hydroperoxide reductase belonging to the family of typical 2-Cys peroxiredoxins with two conserved redox-active cysteines. By similarity to the enzyme from Salmonella typhimurium, AhpC carries out the actual reduction of the hydroperoxide substrate. Under reduced conditions, AhpC forms a decameric ring composed of five homodimers that interact in a head-to-tail configuration, with intermolecular disulfide bonds between Cys47 of one subunit and Cys177 of the second subunit forming the active site . The C terminus is required for the dimer-to-decamer transition, anchors the AhpC-AhpF interaction, and undergoes redox-modulated structural rearrangements . A proteomics screen showed that AhpC interacts with ATP...

## Biological Role

Activated by rpoD (protein.P00579), oxyR (protein.P0ACQ4), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE08|protein.P0AE08]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ahpC; function=+
- `activates` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `S` - regulator=OxyR; target=ahpC; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ahpC; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002090,ECOCYC:EG11384,GeneID:945225`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:638945-639508:+; feature_type=gene
