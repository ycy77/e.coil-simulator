---
entity_id: "protein.P0A9N8"
entity_type: "protein"
name: "nrdG"
source_database: "UniProt"
source_id: "P0A9N8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nrdG yjgE b4237 JW4196"
---

# nrdG

`protein.P0A9N8`

## Static

- Type: `protein`
- Source: `UniProt:P0A9N8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Activation of anaerobic ribonucleoside-triphosphate reductase under anaerobic conditions by generation of an organic free radical, using S-adenosylmethionine and reduced flavodoxin as cosubstrates to produce 5'-deoxy-adenosine. {ECO:0000269|PubMed:1460049, ECO:0000269|PubMed:7852304, ECO:0000269|PubMed:9305874}. The NrdG activase activates the NrdD anaerobic ribonucleoside-triphosphate reductase under anaerobic conditions . Using site-directed mutagenesis, the participation of three cysteine residues in iron chelation in the (4Fe-4S) cluster of this enzyme was demonstrated, but a fourth ligand remained unidentified . An nrdG null mutant does not grow under entirely anaerobic conditions, but grows under aerobic or microaerophilic conditions due to the activity of NrdA and/or NrdB . The activase forms a multi-enzyme complex with flavodoxin-NADP reductase, S-adenosylmethionine (AdoMet) and the anaerobic ribonucleoside triphosphate reductase itself. The activase contains a 4Fe-4S cluster which is reduced by flavodoxin. AdoMet binds to the activase and is in turn reduced to a radical intermediate. The intermediate is cleaved to a 5'-deoxyadenosyl radical and methionine. The 5'-deoxyadenosyl radical generates an essential glycyl radical at Gly681 of anaerobic ribonucleoside triphosphate reductase by abstracting a hydrogen atom...

## Biological Role

Catalyzes protein-glycine,dihydroflavodoxin:S-adenosyl-L-methionine oxidoreductase (S-adenosyl-L-methionine cleaving) (reaction.R04710). Component of anaerobic ribonucleoside-triphosphate reductase activating protein (complex.ecocyc.CPLX0-229), anaerobic nucleoside-triphosphate reductase activating system (complex.ecocyc.NRDACTMULTI-CPLX).

## Annotation

FUNCTION: Activation of anaerobic ribonucleoside-triphosphate reductase under anaerobic conditions by generation of an organic free radical, using S-adenosylmethionine and reduced flavodoxin as cosubstrates to produce 5'-deoxy-adenosine. {ECO:0000269|PubMed:1460049, ECO:0000269|PubMed:7852304, ECO:0000269|PubMed:9305874}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R04710|reaction.R04710]] `KEGG` `database` - via EC:1.97.1.4
- `is_component_of` --> [[complex.ecocyc.CPLX0-229|complex.ecocyc.CPLX0-229]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.NRDACTMULTI-CPLX|complex.ecocyc.NRDACTMULTI-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4237|gene.b4237]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9N8`
- `KEGG:ecj:JW4196;eco:b4237;ecoc:C3026_22870;`
- `GeneID:86861364;948757;`
- `GO:GO:0009265; GO:0015949; GO:0031250; GO:0043365; GO:0046872; GO:0051536; GO:0051539`
- `EC:1.97.1.-`

## Notes

Anaerobic ribonucleoside-triphosphate reductase-activating protein (EC 1.97.1.-) (Class III anaerobic ribonucleotide reductase small component)
