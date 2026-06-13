---
entity_id: "protein.P33596"
entity_type: "protein"
name: "recX"
source_database: "UniProt"
source_id: "P33596"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "recX oraA b2698 JW2668"
---

# recX

`protein.P33596`

## Static

- Type: `protein`
- Source: `UniProt:P33596`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Modulates RecA activity through direct physical interaction. Can inhibit both RecA recombinase and coprotease activities. May have a regulatory role during the SOS response. Inhibits DNA strand exchange in vitro. {ECO:0000269|PubMed:12427742}. RecX is an inhibitor of EG10823-MONOMER RecA. RecX interacts directly with RecA, inhibits its ssDNA-dependent ATPase, coprotease, and DNA strand exchange activities , and blocks the extension of RecA filaments or promotes RecA filament disassembly . RecX itself has weak ssDNA binding activity ; functional competition between EG10976-MONOMER SSB and RecX suggest that an interaction of RecX with ssDNA may be part of the mechanism by which RecX inhibits RecA . RecX binds from the C-terminal domain of one RecA subunit to the nucleotide-binding core of another subunit inhibiting ATPase activity of RecA . The interaction between RecX and RecA itself is modulated by other proteins. RecX competes directly with G6558-MONOMER DinI, a positive modulator of RecA function, for binding to RecA . Both proteins modulate RecA-DNA structures, with dinI being epistatic to recX, which is consistent with DinI acting upstream of RecX . EG10828-MONOMER RecF protects nucleated RecA filaments from RecX inhibition . A structural model of RecX has been proposed, and its interaction with RecA and ssDNA was modeled...

## Annotation

FUNCTION: Modulates RecA activity through direct physical interaction. Can inhibit both RecA recombinase and coprotease activities. May have a regulatory role during the SOS response. Inhibits DNA strand exchange in vitro. {ECO:0000269|PubMed:12427742}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b2698|gene.b2698]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33596`
- `KEGG:ecj:JW2668;eco:b2698;ecoc:C3026_14855;`
- `GeneID:947172;`
- `GO:GO:0005737; GO:0006281; GO:0006282; GO:0006974; GO:0009432; GO:0019899`

## Notes

Regulatory protein RecX (Protein OraA)
