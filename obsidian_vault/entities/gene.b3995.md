---
entity_id: "gene.b3995"
entity_type: "gene"
name: "rsd"
source_database: "NCBI RefSeq"
source_id: "gene-b3995"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3995"
  - "rsd"
---

# rsd

`gene.b3995`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3995`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rsd (gene.b3995) is a gene entity. It encodes rsd (protein.P0AFX4). Encoded protein function: FUNCTION: Binds RpoD and negatively regulates RpoD-mediated transcription activation by preventing the interaction between the primary sigma factor RpoD with the catalytic core of the RNA polymerase and with promoter DNA. May be involved in replacement of the RNA polymerase sigma subunit from RpoD to RpoS during the transition from exponential growth to the stationary phase. {ECO:0000255|HAMAP-Rule:MF_01181, ECO:0000269|PubMed:10368152, ECO:0000269|PubMed:9560209}. EcoCyc product frame: EG11738-MONOMER. EcoCyc synonyms: yjaE. Genomic coordinates: 4196332-4196808. EcoCyc protein note: Rsd exerts its effect via its ability to specifically interact with a number of proteins, including RPOD-MONOMER σ70 , SPOT-MONOMER SpoT and dephosphorylated PTSH-MONOMER HPr . Rsd was first identified as an anti-σ factor. It binds specifically to the major σ factor RPOD-MONOMER σ70 with a stoichiometry of 1:1 . Rsd sequesters σ70, making RNAP core enzyme accessible for σS and possibly other σ factors in stationary phase . The dephosphorylated form of PTSH-MONOMER HPr is able to form a tight 1:1 complex with Rsd and thereby inhibit its interaction with σ70, linking Rsd anti-σ factor activity to nutrient availability...

## Biological Role

Repressed by CueR-Cu+ (complex.ecocyc.CPLX0-10393), ZntR-Zn2+ (complex.ecocyc.CPLX0-10394), [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), DNA-binding transcriptional dual regulator KdpE-phosphorylated (complex.ecocyc.CPLX0-7795), NhaR-Na+ DNA-binding transcriptional activator (complex.ecocyc.MONOMER0-46), fur (protein.P0A9A9), nhaR (protein.P0A9G2), cueR (protein.P0A9G4), and 5 more. Activated by rpoD (protein.P00579), sdiA (protein.P07026), slyA (protein.P0A8W2), lrp (protein.P0ACJ0), rpoS (protein.P13445), rcdA (protein.P75811), mcbR (protein.P76114).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFX4|protein.P0AFX4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (20)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rsd; function=+
- `activates` <-- [[protein.P07026|protein.P07026]] `RegulonDB` `S` - regulator=SdiA; target=rsd; function=+
- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=rsd; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=rsd; function=+
- `activates` <-- [[protein.P75811|protein.P75811]] `RegulonDB` `S` - regulator=RcdA; target=rsd; function=+
- `activates` <-- [[protein.P76114|protein.P76114]] `RegulonDB` `S` - regulator=McbR; target=rsd; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-10393|complex.ecocyc.CPLX0-10393]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.CPLX0-10394|complex.ecocyc.CPLX0-10394]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.CPLX0-7795|complex.ecocyc.CPLX0-7795]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.MONOMER0-46|complex.ecocyc.MONOMER0-46]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=rsd; function=-
- `represses` <-- [[protein.P0A9G2|protein.P0A9G2]] `RegulonDB` `S` - regulator=NhaR; target=rsd; function=-
- `represses` <-- [[protein.P0A9G4|protein.P0A9G4]] `RegulonDB` `S` - regulator=CueR; target=rsd; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=rsd; function=-
- `represses` <-- [[protein.P0ACS5|protein.P0ACS5]] `RegulonDB` `S` - regulator=ZntR; target=rsd; function=-
- `represses` <-- [[protein.P21866|protein.P21866]] `RegulonDB` `S` - regulator=KdpE; target=rsd; function=-
- `represses` <-- [[protein.P23836|protein.P23836]] `RegulonDB|EcoCyc` `S` - regulator=PhoP; target=rsd; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=rsd; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013059,ECOCYC:EG11738,GeneID:948496`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4196332-4196808:-; feature_type=gene
