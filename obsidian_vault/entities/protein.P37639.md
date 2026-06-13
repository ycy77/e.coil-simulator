---
entity_id: "protein.P37639"
entity_type: "protein"
name: "gadX"
source_database: "UniProt"
source_id: "P37639"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gadX yhiX b3516 JW3484"
---

# gadX

`protein.P37639`

## Static

- Type: `protein`
- Source: `UniProt:P37639`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Positively regulates the expression of about fifteen genes involved in acid resistance such as gadA, gadB and gadC. Depending on the conditions (growth phase and medium), can repress gadW. {ECO:0000269|PubMed:11298273, ECO:0000269|PubMed:11976288, ECO:0000269|PubMed:12446650, ECO:0000269|PubMed:12730179, ECO:0000269|PubMed:14617649, ECO:0000269|PubMed:14702398}. The transcriptional activator GadX, for "Glutamic acid decarboxylase," is positively autoregulated and controls the transcription of pH-inducible genes, including the principal acid resistance system , is glutamate dependent (GAD), is also referred to as the GAD system, and its genes are involved in multidrug efflux . In addition GadX also activates the transcription of the central activator involved in the acid response . The physiological inducer is unknown. Richard et al. proposed that GadX can sense intracellular Na+ concentrations, but the mechanism is not known . GadX is one of the regulators of the acid resistance system and is encoded by the unusual gadXW operon, which is located in the region called the acid fitness island . This operon encodes two transcriptional regulators, GadX and GadW, both of which are members of the AraC/XylS family of transcriptional regulators . The activities of GadX and GadW are indispensable upon entry into the stationary phase in response to acid pH...

## Annotation

FUNCTION: Positively regulates the expression of about fifteen genes involved in acid resistance such as gadA, gadB and gadC. Depending on the conditions (growth phase and medium), can repress gadW. {ECO:0000269|PubMed:11298273, ECO:0000269|PubMed:11976288, ECO:0000269|PubMed:12446650, ECO:0000269|PubMed:12730179, ECO:0000269|PubMed:14617649, ECO:0000269|PubMed:14702398}.

## Outgoing Edges (23)

- `activates` --> [[gene.b0485|gene.b0485]] `RegulonDB` `S` - regulator=GadX; target=glsA; function=+
- `activates` --> [[gene.b0486|gene.b0486]] `RegulonDB` `S` - regulator=GadX; target=ybaT; function=+
- `activates` --> [[gene.b1492|gene.b1492]] `RegulonDB` `S` - regulator=GadX; target=gadC; function=+
- `activates` --> [[gene.b1493|gene.b1493]] `RegulonDB` `S` - regulator=GadX; target=gadB; function=+
- `activates` --> [[gene.b3506|gene.b3506]] `RegulonDB` `C` - regulator=GadX; target=slp; function=+
- `activates` --> [[gene.b3507|gene.b3507]] `RegulonDB` `C` - regulator=GadX; target=dctR; function=+
- `activates` --> [[gene.b3508|gene.b3508]] `RegulonDB` `S` - regulator=GadX; target=yhiD; function=-+
- `activates` --> [[gene.b3509|gene.b3509]] `RegulonDB` `S` - regulator=GadX; target=hdeB; function=-+
- `activates` --> [[gene.b3511|gene.b3511]] `RegulonDB` `S` - regulator=GadX; target=hdeD; function=+
- `activates` --> [[gene.b3512|gene.b3512]] `RegulonDB` `S` - regulator=GadX; target=gadE; function=+
- `activates` --> [[gene.b3513|gene.b3513]] `RegulonDB` `S` - regulator=GadX; target=mdtE; function=+
- `activates` --> [[gene.b3514|gene.b3514]] `RegulonDB` `S` - regulator=GadX; target=mdtF; function=+
- `activates` --> [[gene.b3517|gene.b3517]] `RegulonDB` `S` - regulator=GadX; target=gadA; function=+
- `activates` --> [[gene.b4718|gene.b4718]] `RegulonDB` `S` - regulator=GadX; target=gadF; function=+
- `represses` --> [[gene.b1497|gene.b1497]] `RegulonDB` `S` - regulator=GadX; target=ydeM; function=-
- `represses` --> [[gene.b1498|gene.b1498]] `RegulonDB` `S` - regulator=GadX; target=ydeN; function=-
- `represses` --> [[gene.b1583|gene.b1583]] `RegulonDB` `S` - regulator=GadX; target=ynfB; function=-
- `represses` --> [[gene.b1584|gene.b1584]] `RegulonDB` `S` - regulator=GadX; target=speG; function=-
- `represses` --> [[gene.b1634|gene.b1634]] `RegulonDB` `S` - regulator=GadX; target=dtpA; function=-
- `represses` --> [[gene.b3508|gene.b3508]] `RegulonDB` `S` - regulator=GadX; target=yhiD; function=-+
- `represses` --> [[gene.b3509|gene.b3509]] `RegulonDB` `S` - regulator=GadX; target=hdeB; function=-+
- `represses` --> [[gene.b3966|gene.b3966]] `RegulonDB` `S` - regulator=GadX; target=btuB; function=-
- `represses` --> [[gene.b3967|gene.b3967]] `RegulonDB` `S` - regulator=GadX; target=murI; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3516|gene.b3516]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37639`
- `KEGG:ecj:JW3484;eco:b3516;ecoc:C3026_19050;`
- `GeneID:948028;`
- `GO:GO:0000976; GO:0000987; GO:0001216; GO:0003700; GO:0006351; GO:0006974; GO:0042803; GO:0045893`

## Notes

HTH-type transcriptional regulator GadX
