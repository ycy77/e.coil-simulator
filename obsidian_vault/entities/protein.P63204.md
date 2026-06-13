---
entity_id: "protein.P63204"
entity_type: "protein"
name: "gadE"
source_database: "UniProt"
source_id: "P63204"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gadE yhiE yhiT b3512 JW3480"
---

# gadE

`protein.P63204`

## Static

- Type: `protein`
- Source: `UniProt:P63204`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Regulates the expression of several genes involved in acid resistance. Required for the expression of gadA and gadBC, among others, regardless of media or growth conditions. Binds directly to the 20 bp GAD box found in the control regions of both loci. {ECO:0000269|PubMed:12940989, ECO:0000269|PubMed:14702398}. The transcriptional activator GadE, for "Glutamic acid decarboxylase," is positively autoregulated and controls the transcription of genes involved in the maintenance of pH homeostasis, including the principal acid resistance system , glutamate dependent (GAD), also referred as the GAD system, and genes involved in multidrug efflux, among others . GadE also controls the expression of two transcription factors related to acid resistance, GadW and GadX, and for this reason it is considered the central activator of the acid response system . GadE is encoded by the gadE-mdtEF operon, inducible by low pH , which is located in the region called the acid fitness island . Expression of gadE is controlled by an unusually large 798-bp upstream intergenic region, termed the sensory integration locus . At least six regulators related to the acid resistance system, GadE, GadX, GadW, EvgA, YdeO, and MnmE, are involved in the direct regulation of gadE . Ma et al...

## Biological Role

Component of GadE-RcsB DNA-binding transcriptional activator (complex.ecocyc.CPLX0-7852).

## Annotation

FUNCTION: Regulates the expression of several genes involved in acid resistance. Required for the expression of gadA and gadBC, among others, regardless of media or growth conditions. Binds directly to the 20 bp GAD box found in the control regions of both loci. {ECO:0000269|PubMed:12940989, ECO:0000269|PubMed:14702398}.

## Outgoing Edges (19)

- `activates` --> [[gene.b1492|gene.b1492]] `RegulonDB` `C` - regulator=GadE; target=gadC; function=+
- `activates` --> [[gene.b1493|gene.b1493]] `RegulonDB` `C` - regulator=GadE; target=gadB; function=+
- `activates` --> [[gene.b1951|gene.b1951]] `RegulonDB` `S` - regulator=GadE; target=rcsA; function=+
- `activates` --> [[gene.b3212|gene.b3212]] `RegulonDB` `C` - regulator=GadE; target=gltB; function=+
- `activates` --> [[gene.b3213|gene.b3213]] `RegulonDB` `C` - regulator=GadE; target=gltD; function=+
- `activates` --> [[gene.b3214|gene.b3214]] `RegulonDB` `C` - regulator=GadE; target=gltF; function=+
- `activates` --> [[gene.b3491|gene.b3491]] `RegulonDB` `S` - regulator=GadE; target=yhiM; function=+
- `activates` --> [[gene.b3508|gene.b3508]] `RegulonDB` `C` - regulator=GadE; target=yhiD; function=+
- `activates` --> [[gene.b3509|gene.b3509]] `RegulonDB` `S` - regulator=GadE; target=hdeB; function=+
- `activates` --> [[gene.b3510|gene.b3510]] `RegulonDB` `C` - regulator=GadE; target=hdeA; function=+
- `activates` --> [[gene.b3511|gene.b3511]] `RegulonDB` `C` - regulator=GadE; target=hdeD; function=+
- `activates` --> [[gene.b3512|gene.b3512]] `RegulonDB` `S` - regulator=GadE; target=gadE; function=+
- `activates` --> [[gene.b3513|gene.b3513]] `RegulonDB` `S` - regulator=GadE; target=mdtE; function=+
- `activates` --> [[gene.b3514|gene.b3514]] `RegulonDB` `S` - regulator=GadE; target=mdtF; function=+
- `activates` --> [[gene.b3515|gene.b3515]] `RegulonDB` `S` - regulator=GadE; target=gadW; function=+
- `activates` --> [[gene.b3516|gene.b3516]] `RegulonDB` `S` - regulator=GadE; target=gadX; function=+
- `activates` --> [[gene.b4056|gene.b4056]] `RegulonDB` `S` - regulator=GadE; target=yjbQ; function=+
- `activates` --> [[gene.b4057|gene.b4057]] `RegulonDB` `S` - regulator=GadE; target=yjbR; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-7852|complex.ecocyc.CPLX0-7852]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3512|gene.b3512]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P63204`
- `KEGG:ecj:JW3480;eco:b3512;ecoc:C3026_19025;`
- `GeneID:93778473;948023;`
- `GO:GO:0003677; GO:0005667; GO:0006355; GO:1990451`

## Notes

Transcriptional regulator GadE
