---
entity_id: "molecule.ecocyc.FeS-Centers"
entity_type: "small_molecule"
name: "an iron-sulfur cluster"
source_database: "EcoCyc"
source_id: "FeS-Centers"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
  - "an FeS center"
  - "an FeS cluster"
  - "an [FeS] iron-sulfur center"
  - "an [FeS] iron-sulfur cluster"
  - "an iron-sulfur center"
---

# an iron-sulfur cluster

`molecule.ecocyc.FeS-Centers`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:FeS-Centers`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

Iron-sulfur clusters are cofators of FeS-Proteins "iron-sulfur proteins" and consist of a cluster of two to four iron atoms linked to sulfides, some of which are cysteine residues of the protein. Several cluster types have been described, including CPD-6, CPD-23, 3FE-4S and CPD-7. The [3Fe-4S] cluster is relatively rare, and 3Fe/4Fe interconversion may occur with minimal protein reorganization. In another type of Fe-S cluster, known as CPD0-1098, two of the 4 cysteine residues that are coordinated with the iron atoms in regular CPD-6 are substituted by histidine residues. Although the clusters contain several iron atoms, each one usually transfers only one electron, so, for example, a protein with two [4Fe-4S] clusters will usually transfer two electrons. Small electron transfer proteins that contain only [2Fe-2S] or [4Fe-4S] clusters are called Ferredoxins ferredoxins. When Fe-S clusters occur in larger (and sometimes membrane-bound) proteins together with other prosthetic groups and/or metal cofactors, the proteins are designated as complex Fe-S proteins. In addition to their roles in electron t ransfer reactions, iron-sulfur clusters are also known to participate in the activation of substrates, the stabilization of radicals and structures, the protection of proteins from enzymes and the storage of iron and sulfur...

## Biological Role

Binds anaerobic glycerol-3-phosphate dehydrogenase (complex.ecocyc.ANGLYC3PDEHYDROG-CPLX), hydrogenase 2 (complex.ecocyc.CPLX0-8762), glutamate synthase (complex.ecocyc.GLUTAMATESYN-CPLX), nitrate reductase Z (complex.ecocyc.NITRATREDUCTZ-CPLX), rlmC (protein.P75817).

## Annotation

Iron-sulfur clusters are cofators of FeS-Proteins "iron-sulfur proteins" and consist of a cluster of two to four iron atoms linked to sulfides, some of which are cysteine residues of the protein. Several cluster types have been described, including CPD-6, CPD-23, 3FE-4S and CPD-7. The [3Fe-4S] cluster is relatively rare, and 3Fe/4Fe interconversion may occur with minimal protein reorganization. In another type of Fe-S cluster, known as CPD0-1098, two of the 4 cysteine residues that are coordinated with the iron atoms in regular CPD-6 are substituted by histidine residues. Although the clusters contain several iron atoms, each one usually transfers only one electron, so, for example, a protein with two [4Fe-4S] clusters will usually transfer two electrons. Small electron transfer proteins that contain only [2Fe-2S] or [4Fe-4S] clusters are called Ferredoxins ferredoxins. When Fe-S clusters occur in larger (and sometimes membrane-bound) proteins together with other prosthetic groups and/or metal cofactors, the proteins are designated as complex Fe-S proteins. In addition to their roles in electron t ransfer reactions, iron-sulfur clusters are also known to participate in the activation of substrates, the stabilization of radicals and structures, the protection of proteins from enzymes and the storage of iron and sulfur. They can also act as sensors of iron, dioxygen, the superoxide ion, and possibly nitric oxide, and participate in gene expression . In some cases iron-sulfur clusters serve as sources of sulfur in enzymatic reactions. In such cases the cluster needs to be reassembled before the enzyme can catalyze the next round .

## Outgoing Edges (5)

- `binds` --> [[complex.ecocyc.ANGLYC3PDEHYDROG-CPLX|complex.ecocyc.ANGLYC3PDEHYDROG-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-8762|complex.ecocyc.CPLX0-8762]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.GLUTAMATESYN-CPLX|complex.ecocyc.GLUTAMATESYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.NITRATREDUCTZ-CPLX|complex.ecocyc.NITRATREDUCTZ-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[protein.P75817|protein.P75817]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor

## Incoming Edges (0)

_None._

## External IDs

- `EcoCyc:FeS-Centers`
