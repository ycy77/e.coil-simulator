---
entity_id: "protein.P77526"
entity_type: "protein"
name: "yfcG"
source_database: "UniProt"
source_id: "P77526"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yfcG b2302 JW2299"
---

# yfcG

`protein.P77526`

## Static

- Type: `protein`
- Source: `UniProt:P77526`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Exhibits a very robust glutathione (GSH)-dependent disulfide-bond reductase activity toward the model substrate, 2-hydroxyethyl disulfide; the actual physiological substrates are not known. Also has a low GSH-dependent hydroperoxidase activity toward cumene hydroperoxide, but does not reduce H(2)O(2), tert-butyl hydroperoxide, benzyl peroxide, or lauroyl peroxide. Exhibits little or no GSH transferase activity with most typical electrophilic substrates, and has no detectable transferase activity using glutathionylspermidine (GspSH) as the nucleophilic substrate. Is involved in defense against oxidative stress, probably via its peroxidase activity. {ECO:0000269|PubMed:17018556, ECO:0000269|PubMed:19537707}.

## Biological Role

Component of disulfide bond oxidoreductase YfcG (complex.ecocyc.CPLX0-7806).

## Annotation

FUNCTION: Exhibits a very robust glutathione (GSH)-dependent disulfide-bond reductase activity toward the model substrate, 2-hydroxyethyl disulfide; the actual physiological substrates are not known. Also has a low GSH-dependent hydroperoxidase activity toward cumene hydroperoxide, but does not reduce H(2)O(2), tert-butyl hydroperoxide, benzyl peroxide, or lauroyl peroxide. Exhibits little or no GSH transferase activity with most typical electrophilic substrates, and has no detectable transferase activity using glutathionylspermidine (GspSH) as the nucleophilic substrate. Is involved in defense against oxidative stress, probably via its peroxidase activity. {ECO:0000269|PubMed:17018556, ECO:0000269|PubMed:19537707}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7806|complex.ecocyc.CPLX0-7806]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2302|gene.b2302]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77526`
- `KEGG:ecj:JW2299;eco:b2302;ecoc:C3026_12840;`
- `GeneID:93774872;946763;`
- `GO:GO:0004364; GO:0004601; GO:0005737; GO:0006979; GO:0015036; GO:0042803`
- `EC:1.11.1.-; 1.8.4.-`

## Notes

Disulfide-bond oxidoreductase YfcG (EC 1.8.4.-) (GSH-dependent disulfide-bond oxidoreductase YfcG) (GST N1-1) (GST-like protein YfcG) (Organic hydroperoxidase) (EC 1.11.1.-)
