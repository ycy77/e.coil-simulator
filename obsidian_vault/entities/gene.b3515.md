---
entity_id: "gene.b3515"
entity_type: "gene"
name: "gadW"
source_database: "NCBI RefSeq"
source_id: "gene-b3515"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3515"
  - "gadW"
---

# gadW

`gene.b3515`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3515`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gadW (gene.b3515) is a gene entity. It encodes gadW (protein.P63201). Encoded protein function: FUNCTION: Depending on the conditions (growth phase and medium), acts as a positive or negative regulator of gadA and gadBC. Repression occurs directly or via the repression of the expression of gadX. Activation occurs directly by the binding of GadW to the gadA and gadBC promoters. {ECO:0000269|PubMed:12446650, ECO:0000269|PubMed:12730179, ECO:0000269|PubMed:14617649}. EcoCyc product frame: EG12242-MONOMER. EcoCyc synonyms: yhiW. Genomic coordinates: 3663890-3664618. EcoCyc protein note: The transcription factor GadW, for "Glutamic acid decarboxylase," is negatively autoregulated and controls the transcription of the genes involved in the principal acid resistance system, is glutamate dependent (GAD), and is also referred to as the GAD system . In addition, GadW also activates the transcription of the central activator involved in the acid response . The physiological inducer is unknown. Richard et al. proposed that GadW can sense intracellular Na+ concentrations, but the mechanism is not known . The activity of the GadW iModulon decreases in cells evolved on glycerol and lactate as carbon sources . GadW is one of the regulators in the acid resistance system and is encoded by the unusual gadXW operon, which is located in the region called the acid fitness island...

## Biological Role

Repressed by hns (protein.P0ACF8), lrp (protein.P0ACJ0), rutR (protein.P0ACU2), glaR (protein.P37338). Activated by DNA-binding transcriptional dual regulator LldR-S-lactate (complex.ecocyc.CPLX0-7689), lrp (protein.P0ACJ0), zraR (protein.P14375), phoP (protein.P23836), gadE (protein.P63204), ydeO (protein.P76135).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P63201|protein.P63201]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (10)

- `activates` <-- [[complex.ecocyc.CPLX0-7689|complex.ecocyc.CPLX0-7689]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P14375|protein.P14375]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=gadW; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P23836|protein.P23836]] `RegulonDB` `S` - regulator=PhoP; target=gadW; function=+
- `activates` <-- [[protein.P63204|protein.P63204]] `RegulonDB` `S` - regulator=GadE; target=gadW; function=+
- `activates` <-- [[protein.P76135|protein.P76135]] `RegulonDB` `S` - regulator=YdeO; target=gadW; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=gadW; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACU2|protein.P0ACU2]] `RegulonDB` `S` - regulator=RutR; target=gadW; function=-
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=gadW; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011482,ECOCYC:EG12242,GeneID:948029`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3663890-3664618:-; feature_type=gene
