---
entity_id: "protein.P23484"
entity_type: "protein"
name: "fecI"
source_database: "UniProt"
source_id: "P23484"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fecI b4293 JW4253"
---

# fecI

`protein.P23484`

## Static

- Type: `protein`
- Source: `UniProt:P23484`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Sigma factors are initiation factors that promote the attachment of RNA polymerase to specific initiation sites and are then released. This sigma factor regulates transcriptional activation of the fecABCDE operon which mediates ferric citrate transport. {ECO:0000269|PubMed:2254251}. FecI (σ19) belongs to the subfamily of "iron starvation sigmas" within the Extracytoplasmic Function (ECF) family of sigma factors . The only known target for transcription initiation by CPLX0-221 is the fecABCDE operon promoter . This limited role is typical for the minor sigma factors. FecI was first described as a protein that regulates the expression of genes involved in the transport of ferric citrate and was later shown to be the sigma factor that enables transcription from the fec transport operon promoter upstream of fecA . In vitro, transcription by CPLX0-221 is highest at 25°C and is stimulated by the presence of potassium glutamate . Three proteins, EG10286-MONOMER FecA in the outer membrane, EG10292-MONOMER FecR in the cytoplasmic membrane, and FecI in the cytoplasm, form a signaling pathway that responds to the presence of iron(III) dicitrate and induces expression of ferric citrate transport genes (most recently reviewed in ). The periplasmic N terminus of FecA interacts with the C terminus of FecR, and the cytoplasmic N terminus of FecR binds FecI...

## Biological Role

Component of RNA polymerase sigma 19 (complex.ecocyc.CPLX0-221).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Sigma factors are initiation factors that promote the attachment of RNA polymerase to specific initiation sites and are then released. This sigma factor regulates transcriptional activation of the fecABCDE operon which mediates ferric citrate transport. {ECO:0000269|PubMed:2254251}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (6)

- `activates` --> [[gene.b4287|gene.b4287]] `RegulonDB` `C` - sigma=sigma19; target=fecE; function=+
- `activates` --> [[gene.b4288|gene.b4288]] `RegulonDB` `C` - sigma=sigma19; target=fecD; function=+
- `activates` --> [[gene.b4289|gene.b4289]] `RegulonDB` `C` - sigma=sigma19; target=fecC; function=+
- `activates` --> [[gene.b4290|gene.b4290]] `RegulonDB` `C` - sigma=sigma19; target=fecB; function=+
- `activates` --> [[gene.b4291|gene.b4291]] `RegulonDB` `C` - sigma=sigma19; target=fecA; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-221|complex.ecocyc.CPLX0-221]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4293|gene.b4293]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23484`
- `KEGG:ecj:JW4253;eco:b4293;ecoc:C3026_23150;`
- `GeneID:93777538;946839;`
- `GO:GO:0000345; GO:0001000; GO:0001046; GO:0006352; GO:0006355; GO:0006826; GO:0006879; GO:0016987; GO:2000142`

## Notes

Ferric citrate uptake sigma factor FecI
