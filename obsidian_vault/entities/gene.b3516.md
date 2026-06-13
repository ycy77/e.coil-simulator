---
entity_id: "gene.b3516"
entity_type: "gene"
name: "gadX"
source_database: "NCBI RefSeq"
source_id: "gene-b3516"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3516"
  - "gadX"
---

# gadX

`gene.b3516`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3516`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gadX (gene.b3516) is a gene entity. It encodes gadX (protein.P37639). Encoded protein function: FUNCTION: Positively regulates the expression of about fifteen genes involved in acid resistance such as gadA, gadB and gadC. Depending on the conditions (growth phase and medium), can repress gadW. {ECO:0000269|PubMed:11298273, ECO:0000269|PubMed:11976288, ECO:0000269|PubMed:12446650, ECO:0000269|PubMed:12730179, ECO:0000269|PubMed:14617649, ECO:0000269|PubMed:14702398}. EcoCyc product frame: EG12243-MONOMER. EcoCyc synonyms: yhiX. Genomic coordinates: 3664986-3665810. EcoCyc protein note: The transcriptional activator GadX, for "Glutamic acid decarboxylase," is positively autoregulated and controls the transcription of pH-inducible genes, including the principal acid resistance system , is glutamate dependent (GAD), is also referred to as the GAD system, and its genes are involved in multidrug efflux . In addition GadX also activates the transcription of the central activator involved in the acid response . The physiological inducer is unknown. Richard et al. proposed that GadX can sense intracellular Na+ concentrations, but the mechanism is not known . GadX is one of the regulators of the acid resistance system and is encoded by the unusual gadXW operon, which is located in the region called the acid fitness island...

## Biological Role

Repressed by hns (protein.P0ACF8), rutR (protein.P0ACU2), rcsB (protein.P0DMC7), gadW (protein.P63201), nac (protein.Q47005). Activated by rpoD (protein.P00579), adiY (protein.P33234), glaR (protein.P37338), gadW (protein.P63201), gadE (protein.P63204), DNA-binding transcriptional dual regulator TorR-phosphorylated (protein.ecocyc.PHOSPHO-TORR).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37639|protein.P37639]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (11)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gadX; function=+
- `activates` <-- [[protein.P33234|protein.P33234]] `RegulonDB` `S` - regulator=AdiY; target=gadX; function=+
- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=gadX; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P63201|protein.P63201]] `RegulonDB` `S` - regulator=GadW; target=gadX; function=-+
- `activates` <-- [[protein.P63204|protein.P63204]] `RegulonDB` `S` - regulator=GadE; target=gadX; function=+
- `activates` <-- [[protein.ecocyc.PHOSPHO-TORR|protein.ecocyc.PHOSPHO-TORR]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=gadX; function=-
- `represses` <-- [[protein.P0ACU2|protein.P0ACU2]] `RegulonDB` `S` - regulator=RutR; target=gadX; function=-
- `represses` <-- [[protein.P0DMC7|protein.P0DMC7]] `RegulonDB` `C` - regulator=RcsB; target=gadX; function=-
- `represses` <-- [[protein.P63201|protein.P63201]] `RegulonDB` `S` - regulator=GadW; target=gadX; function=-+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=gadX; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011487,ECOCYC:EG12243,GeneID:948028`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3664986-3665810:-; feature_type=gene
